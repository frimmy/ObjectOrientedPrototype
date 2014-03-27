class House(object):


	def __init__(self):
		self.is_built = True	
		self.rooms = 2		
		self.max_rooms = 4
		self.front_yard = True
		self.back_yard = True
		self.name = 'house'
		self.construction_declaration()

	def construction_declaration(self):

		if self.is_built:
			print "Hammer hammer, nail, nail, you'll have you a",self.name,"!"
			print "Your",self.name,"also has",self.rooms,"room(s)!"

		if self.front_yard and self.back_yard:
			print "Your",self.name,"also has a front and back yard! Welcome to the neighborhood!"
 
	def add_room(self):
			if self.rooms < self.max_rooms:
				self.rooms+=1
			else:
				raise Exception("this "+ self.name + " can't add any additional rooms!")
	
	def describe_my_house(self):
		pass

class Mansion(House):
	def __init__(self):
		super(Mansion, self).__init__()
		self.name = 'mansion'
		self.max_rooms = 35
		self.rooms = 6
		self.tennis_court = True
		self.swimming_pool = True

	

class Cottage(House):
	def __init__(self):
		super(Cottage, self).__init__()
		self.name = 'cottage'
		self.rooms = 1
		self.max_rooms = 1	


my_house = House()
my_mansion = Mansion()
my_cottage = Cottage()

print my_house.is_built
print my_mansion.is_built
print my_cottage.is_built
