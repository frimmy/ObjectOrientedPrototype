import unittest
from houses import House, Mansion, Cottage

class TestForHouse(unittest.TestCase):

	def setUp(self):
		self.house = House()
		self.mansion = Mansion()
		self.cottage = Cottage()
		self.buildings = [self.house, self.mansion, self.cottage]

	def classes_was_built_test(self):
		for i in self.buildings:
			self.assertTrue(i.is_built)

	def add_rooms_test(self):
		for i in self.buildings:
			i.add_room()

			self.assertEqual(i.rooms, 3)

	def rename_mansion_class_test(self):
		self.assertEqual(self.mansion.name, 'mansion')	

	def rename_cottage_class_test(self):
		self.assertEqual(self.cottage.name, 'cottage')