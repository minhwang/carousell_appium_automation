from behave import *
from carousell import App, Platform

use_step_matcher("re")

@given('I have a valid email account')
def step_impl(context):
    context.user_id = 'hm8106_test'
    context.user_pwd = '1234'

@when('I login with the valid email account')
def step_impl(context):
    app = App(Platform.ANDROID)
    context.home = app\
                .welcome_view\
                .create(context.wd)\
                .login_with_email()\
                .login(context.user_id, context.user_pwd)
    
@then('The app brings me home')
def step_impl(context):
    assert context.home