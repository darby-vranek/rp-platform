from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')