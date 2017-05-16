Feature: testing correct page title and page url

	@browser
	Scenario: navigating to the correct url
		Given we navigate to the Cake Solutions test website
		when we check the url we are on
		then the url should be https://cakesolutions.github.io/cake-qa-test/#/

	@browser
	Scenario: page has the correct title
		Given we navigate to the Cake Solutions test website2
		when we check the page title
		then the title should be Cake Soloptions FED Test

	Scenario: page return Status Code 200
		Given we navigate to the Cake Solutions test website3
		when we check the status code
		then we should get 200
