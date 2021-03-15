from uuid import uuid4
from exercise_3.common.logger import Logger

class UserRegistration(object):

	def __init__(self) -> None:
		self.users = {}
		self.logger = Logger()

	def register_user(self, user):
		try:
			user_id = str(uuid4())
			self.users[user_id] = user
			self.logger.info("user {} has successfully created".format(user["name"]))
			return user_id
		except Exception as e:
			self.logger.error("cannot create user")
			return None
	
	def delete_user(self, user_id):
		try:
			del self.users[user_id]
			self.logger.info("user_id {} has successfully deleted".format(user_id))
		except Exception as e:
			self.logger.error("cannot delete user")