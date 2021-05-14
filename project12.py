import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("유튜브 채널을 검색하기")
string=input(">> : ")

URL='https://www.youtube.com/'
#options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome(executable_path='C:/Users/mykj6/OneDrive/바탕 화면/202155130_namjuhyeong/chromedriver.exe')#,options=options)

driver.get(url=URL)
search_box = driver.find_element_by_name("search_query")
search_box.send_keys(string)
search_btn=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_btn.click()

driver.get(url = driver.current_url)
setting=driver.find_element_by_xpath('//*[@id="container"]/ytd-toggle-button-renderer')
setting.click()
set_ch=driver.find_elements_by_xpath('//*[@id="label"]')
set_ch6=set_ch[6]
set_ch6.click()

driver.get(url = driver.current_url)
channel = driver.find_element_by_xpath('//*[@id="img"]')
channel.click()

driver.get(url = driver.current_url)
name=driver.find_element_by_xpath('//*[@id="channel-name"]')
print("채널명:",name.text)
subscriber = driver.find_element_by_xpath('//*[@id="subscriber-count"]')
print(subscriber.text,"입니다.")