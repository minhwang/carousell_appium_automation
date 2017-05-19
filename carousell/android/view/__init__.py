from selenium.common.exceptions import TimeoutException, NoSuchElementException
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


class FeatureDialog(CarousellView):
    _id_feature_button = 'com.thecarousell.Carousell:id/feature_button'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            wd.find_element_by_id(cls._id_feature_button)
        except (NoSuchElementException, AssertionError):
            return False
        return True

    @classmethod
    def dismiss(cls, wd):
        wd.find_element_by_id(cls._id_feature_button).click()


