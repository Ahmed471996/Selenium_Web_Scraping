from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv

##driver =webdriver.Chrome(r"G:\Meta World\Data and AI Track\1. Begginer Track\1.Basics\3.Data\3. Data Preparation and Exploration\chromedriver_win32\chromedriver.exe")
s = Service("F:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.amazon.in/gp/bestsellers/books/")

BookTitles = driver.find_elements(By.XPATH,"//div[@class='p13n-sc-truncated']")
prices =driver.find_elements(By.XPATH,"//span[@class='p13n-sc-price']")      #the return value of find_elements is web objects

time.sleep(10)

for i in BookTitles:
    print(i.text)        #text is an attribute in the web object and we want its value for each web object

for i in prices:
    print(i.text)

with open('F:\Products.csv', 'w', encoding="utf-8", newline='') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['book', 'price'])
    for i in range(0,len(prices)):
        csvwriter.writerow([BookTitles[i].text,prices[i].text])