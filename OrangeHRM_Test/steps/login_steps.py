from behave import *
from selenium import webdriver

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when('I enter "{username}" as username')
def step_impl(context, username):
    username_input = context.driver.find_element_by_id("txtUsername")
    username_input.send_keys(username)

@when('I enter "{password}" as password')
def step_impl(context, password):
    password_input = context.driver.find_element_by_id("txtPassword")
    password_input.send_keys(password)

@when('I click on the login button')
def step_impl(context):
    login_button = context.driver.find_element_by_id("btnLogin")
    login_button.click()

@then('I should be logged in successfully')
def step_impl(context):
    assert "dashboard" in context.driver.current_url.lower()
    context.driver.quit()