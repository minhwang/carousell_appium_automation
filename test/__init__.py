import unittest

from appium import webdriver


class AppiumTestCase(unittest.TestCase):
    @classmethod
    def set_desired_capabilities(cls, desired_caps):
        cls._desired_capabilities = desired_caps

    def setUp(self):
        self.wd = webdriver.Remote('http://localhost:4723/wd/hub', self._desired_capabilities)

    def tearDown(self):
        self.wd.quit()



