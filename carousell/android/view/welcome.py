import os

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

from carousell.android.view import CarousellView
from carousell.android.view.login import LoginWithEmail


class Welcome(CarousellView):
    _id_email_sign_in_button = 'com.thecarousell.Carousell:id/email_signin_button'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            wd.find_element_by_id(cls._id_email_sign_in_button)
        except (NoSuchElementException, AssertionError):
            return False
        return True

    def login_with_email(self):
        self.wd.find_element_by_id(self._id_email_sign_in_button).click()
        return LoginWithEmail.create(self.wd)


if __name__ == "__main__":
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        'noReset': False,
        'fullReset': False,
        'app': os.path.join(os.path.dirname(__file__), '../../../Carousell-test-engineering-app.apk'),
        'appPackage': 'com.thecarousell.Carousell',
        'appActivity': 'com.thecarousell.Carousell.activities.WelcomeActivity'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

    Welcome.create(driver).login_with_email()
    driver.quit()
