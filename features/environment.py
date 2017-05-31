from behave import *
from selenium import webdriver
from promise import Promise
from xvfbwrapper import Xvfb

def before_scenario(context, scenario):
	if 'browser' in scenario.tags:
		context.xvfb = Xvfb(width=1280, height=720)
		context.xvfb.start()
		context.driver = webdriver.Firefox()
		context.driver.get('https://cakesolutions.github.io/cake-qa-test/#/')
		return context.driver

def after_scenario(context, scenario):
	if 'browser' in scenario.tags:
		#context.xvfb.stop()
		context.driver.quit()
