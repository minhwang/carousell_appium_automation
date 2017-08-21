Feature: Login
    In order to use the Carousell app
    As a user
    I want to login the app

    Scenario: Successfully login with vaild email account
        Given I have a valid email account
        When I login with the valid email account
        Then The app brings me home