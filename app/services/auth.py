from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.repositories.user import UserRepository


class InvalidCredentialsError(Exception):
    pass


class InactiveUserError(Exception):
    pass


class AuthService:
    @staticmethod
    def authenticate_user(
        db: Session,
        *,
        email: str,
        password: str,
    ) -> str:
        user = UserRepository.get_by_email(
            db=db,
            email=email,
        )

        if user is None:
            raise InvalidCredentialsError(
                "Invalid email or password"
            )

        if not verify_password(
            plain_password=password,
            hashed_password=user.password_hash,
        ):
            raise InvalidCredentialsError(
                "Invalid email or password"
            )

        if not user.is_active:
            raise InactiveUserError(
                "User account is inactive"
            )

        return create_access_token(
            subject=str(user.id),
        )