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
    wait = WebDriverWait(context.driver, 30)
    username_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')))
    assert True == username_input.is_displayed()
    username_input.send_keys(username)

@when('I enter "{password}" as password')
def step_impl(context, password):
    wait = WebDriverWait(context.driver, 30)
    password_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')))
    assert True == password_input.is_displayed()
    password_input.send_keys(password)

@when('I click on the login button')
def step_impl(context):
    wait = WebDriverWait(context.driver, 30)
    login_button = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
    assert True == login_button.is_displayed()
    login_button.click()

@then('I should be logged in successfully')
def step_impl(context):
    wait = WebDriverWait(context.driver, 30)
    dashboard_heading = wait.until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[1]/div[1]/header/div[1]/div[1]/span/h6')))
    assert True == dashboard_heading.is_displayed()
    context.driver.quit()