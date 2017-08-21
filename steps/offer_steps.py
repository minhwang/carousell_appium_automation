from behave import *
from carousell import App, Platform

use_step_matcher("re")

@when('I submit an offer')
def step_impl(context):
    app = App(Platform.ANDROID)
    context.chat = app\
                .welcome_view\
                .create(context.wd)\
                .login_with_email()\
                .login(context.user_id, context.user_pwd)\
                .browse()\
                .browse_category('Cars')\
                .view_product(0)\
                .buy()\
                .submit()\
                .yes()

@then('The app brings me chat')
def step_impl(context):
    assert context.chat