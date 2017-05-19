import os
import unittest

from carousell import Platform, App
from test import AppiumTestCase


class CarousellTestCase(AppiumTestCase):
    def test_GivenValidAccount_WhenLoginWithEmail_ThenBringHome(self):
        app = App(Platform.ANDROID)
        home = app.welcome_view.create(self.wd).login_with_email().login('hm8106_test', '1234')
        self.assertIsNotNone(home)

    def test_GivenValidAccount_WhenSubmitOffer_ThenBringChat(self):
        app = App(Platform.ANDROID)
        chat = app\
            .welcome_view\
            .create(self.wd)\
            .login_with_email()\
            .login('hm8106_test', '1234')\
            .browse()\
            .browse_category('Cars')\
            .view_product(0)\
            .buy()\
            .submit()\
            .yes()
        self.assertIsNotNone(chat)

if __name__ == '__main__':
    caps = {
        'platformName': Platform.ANDROID,
        'deviceName': 'Android Emulator',
        'noReset': False,
        'fullReset': False,
        'app': os.path.join(os.path.dirname(__file__), '../Carousell-test-engineering-app.apk'),
        'appPackage': 'com.thecarousell.Carousell',
        'appActivity': 'com.thecarousell.Carousell.activities.WelcomeActivity'
    }
    AppiumTestCase.set_desired_capabilities(caps)
    suites = unittest.TestLoader().loadTestsFromTestCase(CarousellTestCase)
    unittest.TextTestRunner(verbosity=2).run(suites)