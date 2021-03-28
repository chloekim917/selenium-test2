from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://www.reddit.com/r/DunderMifflin/comments/mf1y4j/makes_it_all_worth_it/'

driver.get(url)

html =  BeautifulSoup(driver.page_source, "html.parser")

result = html.find_all("p",{"class":"_1qeIAgB0cPwnLhDF9XSiJM"})

for item in result:
    print(item.text)
