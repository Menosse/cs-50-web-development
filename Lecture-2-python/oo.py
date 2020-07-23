class Point(object):
	"""docstring for Point"""
	def __init__(self, x, y):
		super(Point, self).__init__()
		self.x = x
		self.y = y

p = Point(2, 8)
print(f"point value x is {p.x} and point value y is {p.y}")

class Flight(object):
	"""docstring for Flight"""
	def __init__(self, capacity):
		self.capacity = capacity
		self.passenger = []

	def open_seats(self):
		return self.capacity - len(self.passenger)

	def add_passenger(self, name):
		if not self.open_seats():
			return False
		else:
			self.passenger.append(name)
			return True

flight = Flight(3)
ppl = ['a', 'b', 'c', 'd']

for person in ppl:
	if flight.add_passenger(person):
		print(f"Added {person} to the flight successfully")
	else:
		print(f"No available seats for {person}")