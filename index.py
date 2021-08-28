from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# entering the keyword
string = str(input('Please enter the keyword you want: '))
x = int(input('How many video links you want: '))

# open the browser for getting the link
driverpath = 'chromedriver.exe'
browser = webdriver.Chrome(executable_path = driverpath)
browser.get('https://www.youtube.com/')

# enter the keyword then click search button
search = WebDriverWait(browser, 20).until(
EC.presence_of_element_located((By.ID, 'search')))
search.send_keys(string)
browser.find_element_by_id('search-icon-legacy').click()

urls = []

for i in range(1, x + 1):
    browser.get('https://www.youtube.com/results?search_query=' + string)
    browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[' + str(i) + ']/div[1]/div/div[1]/div/h3/a/yt-formatted-string').click()
    urls.append(browser.current_url)
browser.close()

for url in urls:
    print(url)