from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver =  webdriver.Chrome()
driver.get("https://sfbay.craigslist.org/")

# wait 30sds before timeout exception
category = 'div.community'
try:
	#element =  WebDriverWait(driver, 30).until(EC.presence__of_element_located((By.CSS_SELECTOR, category)))
	time.sleep(1)
	community = driver.find_element_by_css_selector(category)
	print('ok')
	community = community.find_element_by_tag_name('div')
	print('ok2')
	community = community.find_element_by_tag_name('div')
	print('ok3')
	community = community.find_element_by_tag_name('ul')
	print('ok4')
	community = community.find_elements_by_xpath("//li/a[@href]")
	print('ok5')	
	print(community)
	for item in community:
		print(item.text)
except:
	print(f'could not locate css_selector: {category}')
