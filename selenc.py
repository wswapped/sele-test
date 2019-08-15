from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def getContent(url, method="GET", data = {}):
	# Creating the WebDriver object using the ChromeDriver
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(chrome_options=chrome_options)
	sys.stderr.write(url)
	
	# Directing the driver to the defined url
	driver.get(url)
	#driver.manage().timeouts().pageLoadTimeout(20, TimeUnit.SECONDS);
	try:
		element = WebDriverWait(driver, 30).until(EC.url_changes("uplus.rw"))
	finally:
		driver.quit()

	cont = driver.page_source.encode("utf-8")
	#driver.quit()
	return cont
