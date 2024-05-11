from selenium import webdriver
from selenium.webdriver.common.by import By

#to keep chrome running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
#
# price_item = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(f"The price is {price_item.text}")
event_times=driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# for time in event_times:
#     print(time.text)
event_names=driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events={}

for n in range(len(event_times)):
    events[n] ={
        "time":event_times[n].text,
        "name":event_names[n].text
    }
print(events)
driver.quit()