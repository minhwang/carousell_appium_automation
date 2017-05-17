from selenium.common.exceptions import NoSuchElementException

from carousell.android.view import CarousellView


class Home(CarousellView):
    _id_tabs = 'com.thecarousell.Carousell:id/text_tab'
    _id_view_pager = 'com.thecarousell.Carousell:id/pager'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            wd.find_element_by_id(cls._id_tabs)
            wd.find_element_by_id(cls._id_view_pager)
        except (NoSuchElementException, AssertionError):
            return False
        return True



