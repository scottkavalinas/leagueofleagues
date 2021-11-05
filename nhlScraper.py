import requests
from selenium import webdriver
url ='https://www.quanthockey.com/nhl/seasons/2021-22-nhl-players-stats.html'
browser = webdriver.Chrome()
browser.get(url)

print("STATS")
stats = browser.find_element_by_id('statistics')
print(stats.text)
print("STATS")