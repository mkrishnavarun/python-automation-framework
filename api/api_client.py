from typing import Any

import requests

from exceptions import FrameworkError
from utils.logger import get_logger


class APIClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.logger = get_logger(self.__class__.__name__)

    def request(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )

        except requests.Timeout as exc:
            self.logger.error(
                "Request timed out: %s %s",
                method.upper(),
                url
            )
            raise FrameworkError(
                f"API request timed out: {method.upper()} {url}"
            ) from exc

        except requests.RequestException as exc:
            self.logger.error(
                "API request failed: %s %s - %s",
                method.upper(),
                url,
                exc
            )
            raise FrameworkError(
                f"API request failed: {method.upper()} {url}"
            ) from exc

        self.logger.info(
            "Response status: %s",
            response.status_code
        )


        return response

    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:

        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: Any) -> requests.Response:

        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: Any) -> requests.Response:

        return self.request("PUT", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs: Any) -> requests.Response:

        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:

        return self.request("DELETE", endpoint, **kwargs)

    def close(self) -> None:
        self.session.close()
