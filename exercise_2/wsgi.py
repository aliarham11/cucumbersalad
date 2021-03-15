import falcon
from exercise_2.resources.quotes import QuoteResource

class WSGI(object):

	def __init__(self) -> None:
		super().__init__()

	def create(self):
		quotes_resource = QuoteResource()
		
		app = falcon.API()
		app.add_route("/quotes", quotes_resource)

		return app
