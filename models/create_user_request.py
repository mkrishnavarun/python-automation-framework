from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserRequest:
    name: str
    username: str
    email: str

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "username": self.username,
            "email": self.email
        }