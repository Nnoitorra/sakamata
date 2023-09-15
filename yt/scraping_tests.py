import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass


browser_driver = Service(r'')
page_to_scrape = webdriver.Chrome(service=browser_driver)
page_to_scrape.implicitly_wait(10)
page_to_scrape.get("https://osu.ppy.sh/beatmapsets")
scroll_pause_timer = 2
screen_height = page_to_scrape.execute_script("return window.screen.height;")
i = 1


page_to_scrape.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div[2]/div[4]/button").click()
username = page_to_scrape.find_element(By.NAME, "username")
password = page_to_scrape.find_element(By.NAME, "password")
username.send_keys("")
mypass = getpass.getpass()
password.send_keys(mypass)
page_to_scrape.find_element(By.XPATH, "/html/body/div[5]/div/form/div[5]/div/button").click()

search_term = page_to_scrape.find_element(By.XPATH, "/html/body/div[7]/div/div[2]/div/div[2]/input")
search_term.send_keys("ranked>20161231 ranked<20170201")
page_to_scrape.find_element(By.XPATH, '/html/body/div[7]/div/div[2]/div/div[3]/div[2]/div/a[2]').click()
page_to_scrape.find_element(By.XPATH, '/html/body/div[7]/div/div[2]/div/div[3]/div[3]/div/a[3]').click()
page_to_scrape.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/div/div[1]/div[1]/div/div/a[4]').click()
page_to_scrape.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/div/div[1]/div[1]/div/div/a[4]').click()
time.sleep(2)

while True:
    maps = page_to_scrape.find_elements(By.CLASS_NAME, "beatmapset-panel__info")
    links = page_to_scrape.find_elements(By.CLASS_NAME, "beatmapset-panel__cover-container")
    with open("scraped_maps.csv", "a", newline='') as f:
        writer = csv.writer(f)
        for map, link in zip(maps, links):
            title = map.text.splitlines()
            url = link.get_attribute("href")
            writer.writerow([title[0], url])
    page_to_scrape.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height = screen_height, i = i))
    i += 1
    time.sleep(scroll_pause_timer)
    scroll_height = page_to_scrape.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        break
