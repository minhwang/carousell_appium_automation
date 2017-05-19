from selenium.common.exceptions import NoSuchElementException, WebDriverException

from carousell.android.view import CarousellView, FeatureDialog


class ProductList(CarousellView):
    _id_grid_product = 'com.thecarousell.Carousell:id/grid_product'
    _id_view_product = 'com.thecarousell.Carousell:id/view_product'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            if FeatureDialog.is_in_view(wd):
                FeatureDialog.dismiss(wd)
            wd.find_element_by_id(cls._id_grid_product)
        except (NoSuchElementException, AssertionError):
            return False
        return True

    def view_product(self, idx):
        try:
            self.wd.find_elements_by_id(self._id_view_product)[idx].click()
            return Product.create(self.wd)
        except (WebDriverException, IndexError):
            return None


class Product(CarousellView):
    _id_button_buy = 'com.thecarousell.Carousell:id/button_buy'
    _id_button_chat = 'com.thecarousell.Carousell:id/button_chat'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            while FeatureDialog.is_in_view(wd):
                FeatureDialog.dismiss(wd)
            wd.find_element_by_id(cls._id_button_buy)
            wd.find_element_by_id(cls._id_button_chat)
        except (NoSuchElementException, AssertionError):
            return False
        return True

    def buy(self):
        self.wd.find_element_by_id(self._id_button_buy).click()
        return Offer.create(self.wd)


class Offer(CarousellView):
    _id_submit = 'com.thecarousell.Carousell:id/action_submit'
    _id_text_offer = 'com.thecarousell.Carousell:id/text_offer'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            wd.find_element_by_id(cls._id_submit)
            wd.find_element_by_id(cls._id_text_offer)
        except (NoSuchElementException, AssertionError):
            return False
        return True

    def submit(self):
        self.wd.find_element_by_id(self._id_submit).click()
        return ConfirmOfferDialog.create(self.wd)

    def set_money(self, money):
        self.wd.find_element_by_id(self._id_text_offer).set_value(money)

    def get_money(self):
        return self.wd.find_element_by_id(self._id_text_offer).text


class Chat(CarousellView):
    _id_view_chat = 'com.thecarousell.Carousell:id/view_chat'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            wd.find_element_by_id(cls._id_view_chat)
        except (NoSuchElementException, AssertionError):
            return False
        return True


class ConfirmOfferDialog(CarousellView):
    _id_yes = 'android:id/button1'
    _id_no = 'android:id/button2'

    @classmethod
    def is_in_view(cls, wd):
        try:
            assert super().is_in_view(wd)
            wd.find_element_by_id(cls._id_yes)
            wd.find_element_by_id(cls._id_no)
        except (NoSuchElementException, AssertionError):
            return False
        return True

    def yes(self):
        self.find_element_by_id(self._id_yes).click()
        return Chat.create(self.wd)

    def no(self):
        self.find_element_by_id(self._id_no).click()
        return Offer.create(self.wd)