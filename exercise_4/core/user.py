from uuid import uuid4

class UserDB(object):

	def __init__(self) -> None:
		super().__init__()
		self.users = {}
	
	def get_user(self, user_id):
		try:
			return self.users[user_id]
		except Exception as e:
			return "user not found"

	def add_user(self, user):
		user_id = str(uuid4())
		self.users[user_id] = user
		return user_id
	
	def update_user(self, user_id, user):
		if user_id in self.users:
			self.users[user_id] = user
			return "user updated"
		else:
			return "user not found"

	def delete_user(self, user_id):
		try:
			del self.users[user_id]
			return "user deleted"
		except Exception as e:
			return "user not found"