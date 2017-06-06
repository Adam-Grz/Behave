from behave import *
import requests


#=================================================================================#
@given('we navigate to the Cake Solutions test website')
def step(context):
    pass

@when('we check the url we are on')
def step(context):
    context.correct_url = context.driver.current_url

@then('the url should be https://cakesolutions.github.io/cake-qa-test/#/')
def step(context):
    assert context.correct_url == 'https://cakesolutions.github.io/cake-qa-test/#/'

#=================================================================================#
@given('we navigate to the Cake Solutions test website2')
def step(context):
    pass

@when('we check the page title')
def step(context):
    context.correct_title = context.driver.title

@then('the title should be Cake Soloptions FED Test')
def step(context):
    assert context.correct_title == 'Cake Soloptions FED Test'

#=================================================================================#
@given('we navigate to the Cake Solutions test website3')
def step(context):
    pass

@when('we check the status code')
def step(context):
    context.resp = requests.get('https://cakesolutions.github.io/cake-qa-test/#/')

@then('we should get 200')
def step(context):
    assert context.resp.status_code == 200

#=================================================================================#
