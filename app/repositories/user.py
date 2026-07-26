import uuid
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User, UserRole


class UserRepository:
    @staticmethod
    def get_by_email(
        db: Session,
        email: str,
    ) -> User | None:
        statement = select(User).where(User.email == email)

        return db.scalar(statement)

    @staticmethod
    def get_by_id(
            db: Session,
            user_id: uuid.UUID,
    ) -> User | None:
        statement = select(User).where(User.id == user_id)

        return db.scalar(statement)

    @staticmethod
    def create(
        db: Session,
        *,
        email: str,
        password_hash: str,
        first_name: str,
        last_name: str,
        role: UserRole,
    ) -> User:
        user = User(
            email=email,
            password_hash=password_hash,
            first_name=first_name,
            last_name=last_name,
            role=role,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user