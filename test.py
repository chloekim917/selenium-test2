# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()

# url = 'https://www.youtube.com/watch?v=7UKtY3zp4sA&ab_channel=BjornSteinbekk-Aguywithadrone'

# driver.get(url)

# # print(driver.page_source)

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'style-scope ytd-comment-renderer')))


# html =  BeautifulSoup(driver.page_source, "html.parser")

# result = html.find_all("yt-formatted-string",{"class":"style-scope ytd-comment-renderer"})
# for item in result:
#     print(item.text)


from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://www.reddit.com/r/DunderMifflin/comments/mf1y4j/makes_it_all_worth_it/'

driver.get(url)

html =  BeautifulSoup(driver.page_source, "html.parser")

result = html.find_all("p",{"class":"_1qeIAgB0cPwnLhDF9XSiJM"})
for item in result:
    print(item.text)
