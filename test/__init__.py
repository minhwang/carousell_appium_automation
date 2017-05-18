import unittest

from appium import webdriver


class AppiumTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Remote('http://localhost:4723/wd/hub', self._desired_capabilities)

    def tearDown(self):
        self.wd.quit()
