class House(object):

	is_built = True
	rooms = 2
	front_yard = True
	back_yard = True
	name = 'house'		

	def __init__(self):
		if self.is_built:
			print "Hammer hammer, nail, nail, you'll have you a",self.name,"!"
			

	def add_room(self):
		if self.name = 'mansion':
			self.rooms+=1

class Mansion(House):
	def __init__(self):
		self.name = 'mansion'
		self.rooms = 6
		super(Mansion, self).__init__()

class Cottage(House):
	def __init__(self):
		self.name = 'cottage'
		self.rooms = 1
		super(Cottage, self).__init__()


my_house = House()
my_mansion = Mansion()
my_cottage = Cottage()

print my_house.is_built
print my_mansion.is_built
print my_cottage.is_built