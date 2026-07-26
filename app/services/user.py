from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate


class UserAlreadyExistsError(Exception):
    pass


class UserService:
    @staticmethod
    def create_user(
        db: Session,
        user_data: UserCreate,
    ) -> User:
        existing_user = UserRepository.get_by_email(
            db=db,
            email=user_data.email,
        )

        if existing_user is not None:
            raise UserAlreadyExistsError(
                "User with this email already exists"
            )

        return UserRepository.create(
            db=db,
            email=user_data.email,
            password_hash=hash_password(user_data.password),
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            role=user_data.role,
        )