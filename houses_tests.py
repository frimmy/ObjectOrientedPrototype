import unittest
from houses import House, Mansion, Cottage

class TestForHouse(unittest.TestCase):

	def setUp(self):
		self.house = House()
		self.mansion = Mansion()
		self.cottage = Cottage()

	def house_class_was_built_test(self):
		self.assertTrue(self.house.is_built)

	def mansion_class_exists_test(self):
		self.assertTrue(self.mansion.is_built)

	def cottage_class_exists_test(self):
		self.assertTrue(self.cottage.is_built)
