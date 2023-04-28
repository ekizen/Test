from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(context.driver, 30)
    element = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[1]/img')))
    assert True == element.is_displayed()

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