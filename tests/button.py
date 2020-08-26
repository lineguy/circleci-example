import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_button_in_localhost(self):
        driver = self.driver
        driver.get("http://localhost")

        button = driver.find_element_by_id("Btn")
        button.click()

        text = driver.find_element_by_id("BtnText").text
        assert text == "True"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
