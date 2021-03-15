
class IsEven(object):

	def __init__(self) -> None:
		super().__init__()

	def __call__(self, number):
		try:
			return number % 2 == 0
		except Exception as e:
			return None