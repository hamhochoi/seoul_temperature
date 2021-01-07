from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import time
import datetime
import traceback
from selenium.webdriver.chrome.options import Options
import os
import sys

#PATH = os.getenv("PATH")
#PWD  = os.getcwd()
#os.environ['PATH'] = '{}:{}'.format(PWD, PATH)
#print (os.getenv("PATH"))

#'''
url = 'https://web.kma.go.kr/eng/weather/forecast/current_korea.jsp'

chrome_options = Options()
chrome_options.add_argument("--headless")	
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(executable_path='{}/chromedriver'.format(os.getcwd()), chrome_options=chrome_options)
browser.get(url)
content = browser.page_source
#print (content)
#'''
