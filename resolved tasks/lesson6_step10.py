from selenium import webdriver
import unittest
import time

class TestRequiredFields(unittest.TestCase):
    def test_fields_reg1 (self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('.first_class input[required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.second_class input[required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.third_class input[required]')
        input3.send_keys("some_email")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Welcome text isn't shown")
    def test_fields_reg2 (self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('.first_class input[required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.second_class input[required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.third_class input[required]')
        input3.send_keys("some_email")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Welcome text isn't shown")

if __name__ == "__main__":
    unittest.main()