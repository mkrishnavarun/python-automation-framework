from typing import Any

from api.api_client import APIClient
from models.user import User


class UserService:

    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_user(self, user_id: int) -> User:
        response = self.api_client.get(f"/users/{user_id}")
        response.raise_for_status()

        data = response.json()

        return User(
            id=data["id"],
            name=data["name"],
            username=data["username"],
            email=data["email"]
        )

    def create_user(self, payload: dict[str, Any]) -> User:
        response = self.api_client.post(
            "/users",
            json=payload
        )

        response.raise_for_status()

        data = response.json()

        return User(
            id=data["id"],
            name=data["name"],
            username=data["username"],
            email=data["email"]
        )

    def update_user(
        self,
        user_id: int,
        payload: dict[str, Any]
    ) -> User:

        response = self.api_client.put(
            f"/users/{user_id}",
            json=payload
        )

        response.raise_for_status()

        data = response.json()

        return User(
            id=data["id"],
            name=data["name"],
            username=data["username"],
            email=data["email"]
        )

    def delete_user(self, user_id: int) -> None:
        response = self.api_client.delete(
            f"/users/{user_id}"
        )

        response.raise_for_status()