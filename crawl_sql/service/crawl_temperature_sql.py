from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import time
import datetime
import traceback
from selenium.webdriver.chrome.options import Options
from sql import select, insert 
import os
import sys

PATH = os.getenv("PATH")
print (PATH)
#PWD  = os.getcwd()
#os.environ['PATH'] = '{}:{}'.format(PWD, PATH)
#print (os.getenv("PATH"))
#print (os.listdir("./"))
print (os.getcwd())
print (os.listdir("./"))

url = 'https://web.kma.go.kr/eng/weather/forecast/current_korea.jsp'

def correct_url(url): 
	if not url.startswith("http://") and not url.startswith("https://"):
		url = "http://" + url
	return url

def scrollDown(browser, numberOfScrollDowns):
	body = browser.find_element_by_tag_name("body")
	while numberOfScrollDowns >=0:
		body.send_keys(Keys.PAGE_DOWN)
		numberOfScrollDowns -= 1
		time.sleep(0.3)
	return browser

def crawl_url(url, run_headless=False):
	while (1):
		try:
			url = correct_url(url)
			chrome_options = Options()
			chrome_options.add_argument("--headless")	
			chrome_options.add_argument('--no-sandbox')
			chrome_options.add_argument('--disable-dev-shm-usage')
			browser = webdriver.Chrome(chrome_options=chrome_options)
			browser.get(url)
			#time.sleep(1)
			
			curr_time = str(datetime.datetime.now())
			print (str(curr_time))
			
			content = browser.page_source
			soup = BeautifulSoup(content)
			
			locations = soup.findAll('tr')
			location_infos = []

			for location in locations:
				infos = location.findAll("td")
				
				
				if (infos != []):
					station, weather, visibility, \
					cloud, temp, wind_dir, wind_speed, \
					hum, _, air_pressure 			= infos

					# INSERT to db
					insert(infos)

			browser.quit()
			time.sleep(60)		# Get data one minute / time
			
		except:
			traceback.print_exc()
			
	
if __name__=='__main__':
	crawl_url(url)
	
	
