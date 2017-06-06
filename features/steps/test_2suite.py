from behave import *
import requests

#=================================================================================#
@given('we navigate to the Cake Solutions test website4')
def step(context):
    pass

@when('we check the headers')
def step(context):
    context.resp = requests.get('https://cakesolutions.github.io/cake-qa-test/#/')

@then('the headers should be GitHub.com')
def step(context):
    assert context.resp.headers['server'] == 'GitHub.com'

#=================================================================================#
