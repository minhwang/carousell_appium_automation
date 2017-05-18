from selenium.common.exceptions import NoSuchElementException

from carousell.android.view import CarousellView
from carousell.android.view.home import Home


class LoginWithEmail(CarousellView):
    _id_username = 'com.thecarousell.Carousell:id/text_username'
    _id_password = 'com.thecarousell.Carousell:id/text_password'
    _id_tabs = 'com.thecarousell.Carousell:id/text_tab'
    _id_login_button = 'com.thecarousell.Carousell:id/action_signin'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            wd.find_element_by_id(cls._id_tabs)
        except (NoSuchElementException, AssertionError):
            return False
        return True

    def login(self, username, password):
        self.wd.find_elements_by_id(self._id_tabs)[1].click()
        self.wd.find_element_by_id(self._id_username).set_value(username)
        self.wd.find_element_by_id(self._id_password).set_value(password)
        self.wd.find_element_by_id(self._id_login_button).click()
        return Home.create(self.wd)

    def signup(self):
        pass


class LoginWithFacebook(CarousellView):
    pass


class LoginWithGoogle(CarousellView):
    pass

