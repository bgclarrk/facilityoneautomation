# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .context import sample


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(sample.hmm())

    def test_selenium():
        driver = webdriver.chrome()
        driver.get("https://www.selenium.dev/")
        assert driver.title == "Selenium"
        driver.quit()


if __name__ == "__main__":
    unittest.main()
