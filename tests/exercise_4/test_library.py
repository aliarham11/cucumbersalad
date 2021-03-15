from exercise_4.library import Library

import pytest


def test_valid_borrow_book(mocker):
	lib = Library(book_obj=mocker.Mock(), user_obj=mocker.Mock())
	lib.book.get_book.return_value = {"title": "dummy-title"}
	lib.user.get_user.return_value = {"name": "dummy-name"}
	
	msg = lib.borrow_book(book_id="dummy-book-id", user_id="dummy-user-id")
	
	lib.book.get_book.assert_called_once()
	lib.user.get_user.assert_called_once()
	assert len(lib.trx.keys()) == 1
	assert msg == "user dummy-name has successfully borrowed dummy-title"

def test_invalid_borrow_book(mocker):
	lib = Library(book_obj=mocker.Mock(), user_obj=mocker.Mock())
	
	msg = lib.borrow_book(book_id="dummy-book-id", user_id="dummy-user-id")
	
	assert msg == "data not found"

def test_valid_return_book(mocker):
	lib = Library(book_obj=mocker.Mock(), user_obj=mocker.Mock())
	lib.book.get_book.return_value = {"title": "dummy-title"}
	lib.trx = {"dummy-book-id": {""}}
	msg = lib.return_book("dummy-book-id")
	
	assert len(lib.trx.keys()) == 0
	assert msg == "book dummy-title has sucessfully returned"

def test_invalid_return_book(mocker):
	lib = Library(book_obj=mocker.Mock(), user_obj=mocker.Mock())
	lib.book.get_book.return_value = {"title": "dummy-title"}
	
	msg = lib.return_book("dummy-book-id")
	
	assert msg == "data not found"