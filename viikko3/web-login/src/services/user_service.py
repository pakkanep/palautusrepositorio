from entities.user import User
import re
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if password != password_confirmation:
            raise UserInputError("Given passwords do not match")
        if not username or not password:
            raise UserInputError("Username and password are required")

        if not re.match(r"^(?=.*[a-z])(?=.*\d).{8,}$", password):
            raise UserInputError("Password has to be atleast 8 characters long and consist of letters and atleast 1 number")
        
        if not re.match(r"^[a-z]{3,}$", username):
            raise UserInputError("Username has to consist of 3 characters minimum")


user_service = UserService()
