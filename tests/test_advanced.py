# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

HOME_PAGE_URL = "https://corp.facilityone.com"
DEMO_FORM_URL = "https://corp.facilityone.com/qa-test-assessment"
DEMO_CONFIRMATION_TEXT = (
    "Thanks for booking a demo! We look forward to meeting with you."
)


class AdvancedTestSuite(unittest.TestCase):
    """Check content on home page and verify demo form submit"""

    def test_facilityone_homepage_content(self):
        """verify the title of the page"""

        driver = webdriver.Chrome()
        driver.get(HOME_PAGE_URL)
        assert driver.title == "FacilityONE"
        driver.quit()

    def test_facilityone_demo_form_submit(self):
        """submit the contact form"""
        driver = webdriver.Chrome()
        driver.get(DEMO_FORM_URL)

        WebDriverWait(driver, 5)

        # Check if chat window is open and close if displayed
        try:
            chat_close = driver.find_element(
                By.CLASS_NAME, "CommonWelcomeMessageContent__CloseButton-sc-619ctl-0"
            )
            if chat_close.is_displayed():
                chat_close.click()
        except NoSuchElementException:
            print("Element Not Found")

        # Check if cookies window is open and accept if displayed
        try:
            accept_cookies = driver.find_element(By.ID, "hs-eu-opt-in-buttons")
            if accept_cookies.is_displayed():
                accept_cookies.click()
        except NoSuchElementException:
            print("Element Not Found")

        # Grab elements from demo form
        first_name = driver.find_element(
            By.ID, "firstname-172110b4-03a7-4430-8917-b3e674e895da_7474"
        )
        last_name = driver.find_element(
            By.ID, "lastname-172110b4-03a7-4430-8917-b3e674e895da_7474"
        )
        business_email = driver.find_element(
            By.ID, "email-172110b4-03a7-4430-8917-b3e674e895da_7474"
        )
        phone_number = driver.find_element(
            By.ID, "phone-172110b4-03a7-4430-8917-b3e674e895da_7474"
        )
        organization = driver.find_element(
            By.ID, "company-172110b4-03a7-4430-8917-b3e674e895da_7474"
        )
        job_title = driver.find_element(
            By.ID, "jobtitle-172110b4-03a7-4430-8917-b3e674e895da_7474"
        )
        industry = driver.find_element(
            By.XPATH, '//select[@name="0-2/industry"]/option[text()="Education"]'
        )
        submit = driver.find_element(
            By.XPATH,
            '//*[@id="hsForm_172110b4-03a7-4430-8917-b3e674e895da_7474"]/div[9]/div[2]/input',
        )

        # Enter inputs into the form
        first_name.send_keys("Brian")
        last_name.send_keys("Clark")
        business_email.send_keys("bgclarrk@gmail.com")
        phone_number.send_keys("480-634-0600")
        organization.send_keys("FacilityONE")
        job_title.send_keys("QA Engineer")
        industry.click()
        submit.click()

        # Verify the confirmation message is displayed
        WebDriverWait(driver, 5)
        assert DEMO_CONFIRMATION_TEXT in driver.page_source
        driver.quit()


if __name__ == "__main__":
    unittest.main()
