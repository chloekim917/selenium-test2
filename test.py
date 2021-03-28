from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')

url = 'https://www.youtube.com/watch?v=7UKtY3zp4sA&ab_channel=BjornSteinbekk-Aguywithadrone'

driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'u_cbox_area')))

html =  BeautifulSoup(driver.page_source, "html.parser")

result = html.find_all("div",{"class":"style-scope ytd-comment-renderer"})
for item in result:
    print(item.text)


