from selenium import webdriver
url ='https://www.baseball-reference.com/leagues/majors/2021-batting-leaders.shtml'
browser = webdriver.Chrome()
browser.get(url)
print("STATS")
stats = browser.find_element_by_id('div_leaderboard_batting')
print(stats.text)
print("STATS")