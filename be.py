from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import re


# driver = webdriver.Chrome()
# sleep(5)
driver = webdriver.Remote(  command_executor='http://localhost:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

url = 'http://textfiles.com/stories/alissadl.txt'
driver.get(url)

html =  BeautifulSoup(driver.page_source, "html.parser")

for item in html:
    actual_text=item.text

driver.close() 

def freq(actual_text): 
    #eliminate special characters
    new_string = re.sub(r'[^a-zA-Z0-9 ]','',actual_text)
    # break the string into list of words
    str_list = new_string.casefold().split()

  
    # set of unique words 
    unique_words = set(str_list) 
      
    arr = []

    #words count string and array creation
    for words in unique_words : 
        print(words,':', str_list.count(words)) 
        arr.append(words + ': ' + str(str_list.count(words)))
    return arr
  
# driver code 
if __name__ == "__main__": 
    actual_text
    # calling the freq function 
    freq(actual_text) 

#json
app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def get_wordcount():
    return jsonify({'words': freq(actual_text)})



