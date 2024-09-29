import pytest
from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from src.models import User
from src.user.schemas import UserCreate
from src.user.service import UserService

from src.user.service import UserService


@pytest.fixture
def user_create_data():
    return UserCreate(
        name="Test User", email="test@example.com", password="testpassword"
    )


@pytest.fixture
def mock_db(mocker):
    mock_db = mocker.MagicMock(spec=Session)
    return mock_db


def test_create_user_success(mock_db, user_create_data):
    user_service = UserService(db=mock_db)

    mock_db.query.return_value.filter.return_value.first.return_value = None

    created_user = user_service.create_user(user_create_data)

    assert created_user.name == user_create_data.name
    assert created_user.email == user_create_data.email
    assert user_service.verify_password(
        user_create_data.password, created_user.password
    )
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(created_user)


def test_create_user_email_already_exists(mock_db, user_create_data):
    user_service = UserService(db=mock_db)

    existing_user = User(
        name="Existing User", email=user_create_data.email, password="hashedpassword"
    )
    mock_db.query.return_value.filter.return_value.first.return_value = existing_user

    with pytest.raises(HTTPException) as excinfo:
        user_service.create_user(user_create_data)

    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Email already in use"
    mock_db.add.assert_not_called()
    mock_db.commit.assert_not_called()
    mock_db.refresh.assert_not_called()
