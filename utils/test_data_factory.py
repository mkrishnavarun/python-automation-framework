import uuid

from models.create_user_request import CreateUserRequest


class TestDataFactory:

    @staticmethod
    def create_user_request() -> CreateUserRequest:
        unique_id = uuid.uuid4().hex[:8]

        return CreateUserRequest(
            name=f"Automation User {unique_id}",
            username=f"automation_{unique_id}",
            email=f"automation_{unique_id}@test.com"
        )