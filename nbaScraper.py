from selenium import webdriver
url ='https://www.basketball-reference.com/leagues/NBA_2021_per_game.html'
browser = webdriver.Chrome()
browser.get(url)
print("STATS")
stats = browser.find_element_by_id('per_game_stats')
print(stats.text)
print("STATS")