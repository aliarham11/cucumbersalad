from uuid import uuid4

class BookShelf(object):

	def __init__(self) -> None:
		super().__init__()

	def __init__(self) -> None:
		super().__init__()
		self.books = {}
	
	def get_book(self, book_id):
		try:
			return self.books[book_id]
		except Exception as e:
			return "book not found"

	def add_book(self, book):
		book_id = str(uuid4())
		self.books[book_id] = book
		return book_id
	
	def update_book(self, book_id, book):
		try:
			self.books[book_id] = book
			return "book updated"
		except Exception as e:
			return "book not found"

	def delete_book(self, book_id):
		try:
			del self.books[book_id]
			return "book deleted"
		except Exception as e:
			return "book not found"