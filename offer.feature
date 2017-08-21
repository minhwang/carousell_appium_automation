Feature: Offer
    As a user
    I should be able to offer the price

    Scenario: Successfully submit an offer
        Given I have a valid email account
        When I submit an offer
        Then The app brings me chat