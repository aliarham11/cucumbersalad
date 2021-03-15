from exercise_4.core.book import BookShelf


def test_valid_add_n_delete_book():
	bookshelf = BookShelf()
	bid = bookshelf.add_book({
		"title": "Continuous Delivery",
		"author": "Jez Humble & David Farley"
	})

	assert len(bookshelf.books.keys()) == 1

	bookshelf.delete_book(book_id=bid)

	assert len(bookshelf.books.keys()) == 0

def test_invalid_delete_book():
	bookshelf = BookShelf()
	
	msg = bookshelf.delete_book("dummy_id")

	assert msg == "book not found"

def test_valid_add_n_get_book():
	bookshelf = BookShelf()
	expected = {
		"title": "Continuous Delivery",
		"author": "Jez Humble & David Farley"
	}
	bid = bookshelf.add_book(book=expected)

	assert len(bookshelf.books.keys()) == 1

	actual = bookshelf.get_book(book_id=bid)

	assert expected == actual

def test_invalid_get_book():
	bookshelf = BookShelf()
	
	msg = bookshelf.get_book("dummy_id")

	assert msg == "book not found"

def test_valid_add_n_update_book():
	bookshelf = BookShelf()
	book = {
		"title": "Continuous Delivery",
		"author": "Jez Humble & David Farley"
	}

	expected = {
		"title": "Continuous Delivery - Part 2",
		"author": "Jez Humble & David Farley"
	}

	bid = bookshelf.add_book(book=book)

	assert len(bookshelf.books.keys()) == 1

	msg = bookshelf.update_book(book_id=bid, book=expected)
	actual = bookshelf.get_book(book_id=bid)

	assert msg == "book updated"
	assert expected == actual

def test_invalid_update_book():
	bookshelf = BookShelf()
	
	msg = bookshelf.update_book(book_id="dummy_id", book={})

	assert msg == "book not found"