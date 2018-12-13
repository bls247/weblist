from selenium import webdriver

import unittest

class NewUserTest(unittest.TestCase):


	def setUp(self):
		self.browser = webdriver.Firefox()


	def tearDown(self):
		self.browser.quit()	


	def test_to_start_a_list_and_retrieve_it_later(self):

		# Mary has heard about a new online to-do app

		# She visits the site to check it out

		self.browser.get('http://localhost:8000')

		# She observes the page title and header mentions to-do list

		self.assertIn('To-Do',self.browser.title)

		self.fail('Test not finsihed yet!')

		# She is prompted to enter a to-do item when page loads

		# She types "Buy a macbook" into the textbox presented

		# When she hits enter ,the page updates and lists
		# "1" Buy macbook" as an item in a to-do list

		#The textbox prompts her to add another item.

		# She types "Create a new course"

		#The page updates again, and shows both items on her list

		# Mary hopes the site will remember her list.

		# She observes the site generated a unique URL

		# She visits the URL and observes her to-do list is there.

		# Mary pleased her list is saved and exits

if __name__ == '__main__':
	unittest.main()