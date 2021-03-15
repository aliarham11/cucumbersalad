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


# Sample run
if __name__ == "__main__":
	book_shelf = BookShelf()
	user_db = UserDB()

	bid1 = book_shelf.add_book({
		"title": "Continuous Delivery",
		"author": "Jez Humble & David Farley"
	})

	bid2 = book_shelf.add_book({
		"title": "Algorithms",
		"author": "Robert Sedgewick & Kevin Wayne"
	})

	bid3 = book_shelf.add_book({
		"title": "The Self-Taught Programmer",
		"author": "Cory Althoff"
	})

	uid1 = user_db.add_user({
		"name": "Peter Seibel"
	})

	uid2 = user_db.add_user({
		"name": "Eric Evans"
	})

	uid3 = user_db.add_user({
		"name": "Donald E. Knuth"
	})

	my_library = Library(book_obj=book_shelf, user_obj=user_db)
	
	msg = my_library.borrow_book(user_id=uid1, book_id=bid2)
	print(msg)

	msg = my_library.borrow_book(user_id=uid2, book_id=bid1)
	print(msg)

	msg = my_library.return_book(bid2)
	print(msg)
