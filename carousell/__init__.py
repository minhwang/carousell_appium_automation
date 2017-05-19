import importlib


class Platform:
    ANDROID = 'Android'
    IOS = 'iOS'


class App:
    def __init__(self, platform):
        self._platform = platform

    @property
    def welcome_view(self):
        name = 'carousell.{}.view.welcome'.format(self._platform.lower())
        return getattr(importlib.import_module(name), 'Welcome')


