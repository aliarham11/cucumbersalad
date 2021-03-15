from exercise_4.core.book import BookShelf
from exercise_4.core.user import UserDB

class Library(object):

	def __init__(self, book_obj: BookShelf, user_obj: UserDB) -> None:
		super().__init__()
		self.trx = {}
		self.book = book_obj
		self.user = user_obj

	def borrow_book(self, user_id, book_id):
		try:
			_book = self.book.get_book(book_id)
			_user = self.user.get_user(user_id)

			self.trx[book_id] = {
				"user": _user,
				"book": _book
			}

			return "user {user} has successfully borrowed {book}".format(user=_user["name"], book=_book["title"])
		except Exception as e:
			print(e)
			return "data not found"
	
	def return_book(self, book_id):
		try:
			_book = self.book.get_book(book_id)
			del self.trx[book_id]
			
			return "book {book} has sucessfully returned".format(book=_book["title"])
		except Exception as e:
			return "data not found"
