from selenium import webdriver
url ='https://www.pro-football-reference.com/years/2021/index.htm'
browser = webdriver.Chrome()
browser.get(url)
print("STATS")
stats = browser.find_element_by_id('AFC')
print(stats.text)
print("STATS")