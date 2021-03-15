from uuid import uuid4
from exercise_3.main import UserRegistration

import pytest


def test_register_valid_user(mocker):
	user_r = UserRegistration()
	
	mock_patcher = mocker.patch.object(user_r.logger, "info")

	user_r.register_user(user={"name": "Fulan"})

	mock_patcher.assert_called_once()
	mock_patcher.assert_called_with("user Fulan has successfully created")


def test_register_invalid_user(mocker):
	user_r = UserRegistration()
	user_r.users = None
	
	mock_patcher = mocker.patch.object(user_r.logger, "error")

	user_r.register_user(user={"name": "Fulan"})

	mock_patcher.assert_called_once()
	mock_patcher.assert_called_with("cannot create user")

def test_delete_user_valid(mocker):
	user_r = UserRegistration()
	mock_patcher = mocker.patch.object(user_r.logger, "info")
	
	uid = user_r.register_user(user={"name": "Fulan"})

	user_r.delete_user(user_id=uid)

	mock_patcher.call_count == 2
	mock_patcher.assert_called_with("user_id {} has successfully deleted".format(uid))

def test_delete_user_invalid(mocker):
	user_r = UserRegistration()
	mock_patcher = mocker.patch.object(user_r.logger, "error")

	user_r.delete_user(user_id=uuid4())

	mock_patcher.assert_called_once()
	mock_patcher.assert_called_with("cannot delete user")