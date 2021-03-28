from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')

url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=421&aid=0004932341'

driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'u_cbox_area')))

html =  BeautifulSoup(driver.page_source, "html.parser")

result = html.find_all("span",{"class":"u_cbox_contents"})
for item in result:
    print(item.text)


