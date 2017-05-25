from behave import *
from selenium import webdriver
from promise import Promise

def before_scenario(context, scenario):
	if 'browser' in scenario.tags:
		context.driver = webdriver.Firefox("/features")
		context.driver.set_window_size(1500, 1000)
		context.driver.maximize_window()
		context.driver.get('https://cakesolutions.github.io/cake-qa-test/#/')
		return context.driver

def after_scenario(context, scenario):
	if 'browser' in scenario.tags:
		context.driver.quit()
