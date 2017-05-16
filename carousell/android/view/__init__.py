from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class CarousellView:
    def __init__(self, wd):
        self.wd = wd

    @classmethod
    def is_in_view(cls, wd):
        return True

    @classmethod
    def create(cls, wd):
        try:
            WebDriverWait(wd, 10).until(cls.is_in_view)
        except TimeoutException:
            return None
        return cls(wd)

