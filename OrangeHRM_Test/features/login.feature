Feature: Login to OrangeHRM
    As a user
    I want to log in to OrangeHRM
    So that I can access the application

Scenario: Login with valid credentials
    Given I am on the login page
    When I enter "Admin" as username
    And I enter "admin123" as password
    And I click on the login button
    Then I should be logged in successfully