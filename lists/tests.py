from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


# self represents the instance of the class.
# By using self keyword we can access the attribute
#and methods of the class in python.

class HomePageTest(TestCase):

	def test_root_url_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
