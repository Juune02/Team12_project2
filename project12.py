import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("구독자 수가 궁금한 채널명을 입력")
string=input(">> : ")

URL='https://www.youtube.com/'
#options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome(executable_path='C:/Users/mykj6/OneDrive/바탕 화면/202155130_namjuhyeong/chromedriver.exe')#,options=options)
driver.get(url=URL)

search_box = driver.find_element_by_name("search_query")
search_box.send_keys(string)
search_btn=driver.find_element_by_class_name("style-scope ytd-searchbox")
search_btn.send_keys(Keys.ENTER)


driver.get(url = driver.current_url)
channel = driver.find_element_by_xpath('//*[@id="img"]')
channel.click()
driver.get(url = driver.current_url)
subscriber = driver.find_element_by_xpath('//*[@id="subscriber-count"]')
print(subscriber.text)
