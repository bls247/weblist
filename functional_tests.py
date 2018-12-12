from selenium import webdriver

browser = webdriver.Firefox()

#browser = webdriver.Chrome()

browser.get('http://localhost:8000')


assert 'Django' in browser.title

# No quit function is specified so browser does not close
# after failed functional test.

# You can use either chrome or firefox with selenium