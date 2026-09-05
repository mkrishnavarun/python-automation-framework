import requests


class ResponseValidator:

    @staticmethod
    def assert_status_code(
        response: requests.Response,
        expected_status: int
    ) -> None:

        assert response.status_code == expected_status, (
            f"Expected status code {expected_status}, "
            f"but received {response.status_code}. "
            f"Response: {response.text}"
        )

    @staticmethod
    def assert_json_field(
        response: requests.Response,
        field: str,
        expected_value
    ) -> None:

        data = response.json()

        assert field in data, (
            f"Field '{field}' not found in response: {data}"
        )

        assert data[field] == expected_value, (
            f"Expected {field}={expected_value}, "
            f"but received {data[field]}"
        )