from selenium.common.exceptions import NoSuchElementException

from carousell.android.view import CarousellView
from carousell.android.view.product import ProductList


class Home(CarousellView):
    _id_tab = 'com.thecarousell.Carousell:id/text_tab'
    _id_action_inbox = 'com.thecarousell.Carousell:id/action_inbox'
    _id_action_social = 'com.thecarousell.Carousell:id/action_social'
    _id_action_search = 'com.thecarousell.Carousell:id/action_search'
    _id_action_sell = 'com.thecarousell.Carousell:id/action_sell'
    _id_view_pager = 'com.thecarousell.Carousell:id/pager'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            wd.find_element_by_id(cls._id_tab)
            wd.find_element_by_id(cls._id_view_pager)
        except (NoSuchElementException, AssertionError):
            return False
        return True

    def browse(self):
        self.wd.find_elements_by_id(self._id_tab)[0].click()
        return Browse.create(self.wd)

    def groups(self):
        self.wd.find_elements_by_id(self._id_tab)[1].click()
        return Groups.create(self.wd)

    def activity(self):
        self.wd.find_elements_by_id(self._id_tab)[2].click()
        return Activity.create(self.wd)

    def me(self):
        self.wd.find_elements_by_id(self._id_tab)[3].click()
        return Me.create(self.wd)


class Browse(Home):
    _id_list_collection = 'com.thecarousell.Carousell:id/list_collection'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            wd.find_element_by_id(cls._id_list_collection)
        except (NoSuchElementException, AssertionError):
            return False
        return True

    def browse_category(self, category_name):
        el = self.wd.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("' + category_name + '").instance(0));')
        el.click()
        return ProductList.create(self.wd)


class Groups(Home):
    pass


class Activity(Home):
    pass


class Me(Home):
    pass



