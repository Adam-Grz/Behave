#noinspection CucumberUndefinedStep
Feature: testing response

    Scenario: navigating to the correct url
        Given we navigate to the Cake Solutions test website4
        when we check the headers
        then the headers should be GitHub.com