import os

from appium import webdriver

if __name__ == "__main__":
    desired_capabilities = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        'noReset': True,
        'fullReset': False,
        'app': os.path.join(os.path.dirname(__file__), '../../../Carousell-test-engineering-app.apk'),
        'appPackage': 'com.thecarousell.Carousell',
        'appActivity': 'com.thecarousell.Carousell.activities.WelcomeActivity'
    }
    webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

