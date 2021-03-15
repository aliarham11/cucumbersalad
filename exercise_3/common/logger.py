
class Logger(object):

	def info(self, msg):
		print("INFO: {}".format(msg))

	def debug(self, msg):
		print("DEBUG: {}".format(msg))

	def warning(self, msg):
		print("WARNING: {}".format(msg))
	
	def error(self, msg):
		print("ERROR: {}".format(msg))

	def critical(self, msg):
		print("CRITICAL: {}".format(msg))
