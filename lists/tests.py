from django.test import TestCase


# self represents the instance of the class.
# By using self keyword we can access the attribute
#and methods of the class in python.

class SmokeTest(TestCase):

	def test_bad_addition(self):
		self.assertEqual(7 + 7 , 13)
