def announce(x):
	def wrapper():
		print("about to run the function")
		x()
		print("done with the function")
	return wrapper

@announce
def hello():
	print("hello, world!")

hello()