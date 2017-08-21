import os

from appium import webdriver
from carousell import Platform

def before_feature(context, feature):
    caps = {
        'platformName': Platform.ANDROID,
        'deviceName': 'Android Emulator',
        'noReset': False,
        'fullReset': True,
        'app': os.path.join(os.path.dirname(__file__), './Carousell-test-engineering-app.apk'),
        'appPackage': 'com.thecarousell.Carousell',
        'appActivity': 'com.thecarousell.Carousell.activities.WelcomeActivity'
    }

    wd = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    context.wd = wd

def after_feature(context, feature):
    context.wd.quit()
