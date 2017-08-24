from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
from time import sleep
from xlsxwriter.workbook import Workbook
from PIL import Image
import os
import ImageGrab
import datetime
import io
import random, string
import subprocess
import sys
from testrail2 import *



start_time = time.time()

with open('testrailrunid.txt', 'r') as f:
	run_id = f.read()

f.close()

with open('resultsfilename.txt', 'r') as f:
	resultsfile = f.read()

case_id = 139


argument = sys.argv[1]

if argument == "1":
	driver = webdriver.Chrome('chromedriver.exe')
elif argument == "2":
	driver = webdriver.Ie('IEdriverserver.exe')


def get_testrail_client():
	with open('testrailurl.txt', 'r') as f:
		testrail_url = f.read()

	f.close()
	
	client = APIClient(testrail_url)

	with open('testraillogin.txt', 'r') as l:
		client.user = l.read()

	l.close()


	with open('testrailpassword.txt', 'r') as p:
		client.password = p.read()

	p.close()

	return client


def update_testrail(case_id,run_id,result_flag):
	"Update TestRail for a given run_id and case_id"
	update_flag = False
	#Get the TestRail client account details
	client = get_testrail_client()
 
	#Update the result in TestRail using send_post function. 
	#Parameters for add_result_for_case is the combination of runid and case id. 
	#status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
	status_id = 1 if result_flag is True else 5

 
	if run_id is not None:
		try:
			result = client.send_post(
				'add_result_for_case/%s/%s'%(run_id,case_id),
				{'status_id': status_id })
		except Exception,e:
			print 'Exception in update_testrail() updating TestRail.'
			print 'PYTHON SAYS: '
			print e
		else:
			print 'Updated test result for case: %s in test run: %s'%(case_id,run_id)
		
	return update_flag


def fullpage_screenshot(driver, file):

		print("Starting chrome full page screenshot workaround ...")

		total_width = driver.execute_script("return document.body.offsetWidth")
		total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
		viewport_width = driver.execute_script("return document.body.clientWidth")
		viewport_height = driver.execute_script("return window.innerHeight")
		print("Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height,viewport_width,viewport_height))
		rectangles = []

		i = 0
		while i < total_height:
			ii = 0
			top_height = i + viewport_height

			if top_height > total_height:
				top_height = total_height

			while ii < total_width:
				top_width = ii + viewport_width

				if top_width > total_width:
					top_width = total_width

				print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
				rectangles.append((ii, i, top_width,top_height))

				ii = ii + viewport_width

			i = i + viewport_height

		stitched_image = Image.new('RGB', (total_width, total_height))
		previous = None
		part = 0

		for rectangle in rectangles:
			if not previous is None:
				driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
				print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
				time.sleep(0.2)

			file_name = "part_{0}.png".format(part)
			print("Capturing {0} ...".format(file_name))

			driver.get_screenshot_as_file(file_name)
			screenshot = Image.open(file_name)

			if rectangle[1] + viewport_height > total_height:
				offset = (rectangle[0], total_height - viewport_height)
			else:
				offset = (rectangle[0], rectangle[1])

			print("Adding to stitched image with offset ({0}, {1})".format(offset[0],offset[1]))
			stitched_image.paste(screenshot, offset)

			del screenshot
			os.remove(file_name)
			part = part + 1
			previous = rectangle

		stitched_image.save(file)
		print("Finishing chrome full page screenshot workaround...")
		return True

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

def randomnumber(i):
	return ''.join(random.choice(string.digits) for _ in range(i))


with open('CCaddress.txt', 'r') as f:
	CC = f.read()

f.close()

with open('login.txt', 'r') as l:
	login = l.read()

l.close()

with open('password.txt', 'r') as p:
	passw = p.read()

p.close()


driver.get(CC);

driver.maximize_window()

wait = WebDriverWait(driver, 15)

username = '//*[@id="ng-view"]/div[2]/div[1]/div[1]/input'
password = '//*[@id="ng-view"]/div[2]/div[1]/div[2]/input'

wait.until(EC.presence_of_element_located((By.XPATH, username)))

driver.find_element_by_xpath(username).clear()

driver.find_element_by_xpath(password).clear()

driver.find_element_by_xpath(username).send_keys('group@cctrial.co.uk')
driver.find_element_by_xpath(password).send_keys('redLorry2')

sleep(0.5)

driver.find_element_by_xpath('//*[@id="ng-view"]/div[2]/div[2]/button').click() # Sign in button

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ng-view"]/div[3]/div/div[1]/a[1]'))) # Monitoring

sleep(0.2)

testy = "QWERTYfdsgd"

try:
	testy = driver.find_element_by_xpath('//*[@id="ng-view"]/div[3]/div/div[1]/a[1]')
except:
	pass


def presence(qqq):
	with open("a.txt", 'w') as f:
		assert "%s" % qqq in driver.page_source, f.write("Log in failed!")
		f.write("SUCCESS!")
	f.close()
	return "SUCCESS!"

print presence("Show all")



driver.save_screenshot("1aValidLogin.png")

sleep(0.5)



#result_flag = True

#	update_testrail(case_id,run_id,result_flag=True)


driver.quit()
