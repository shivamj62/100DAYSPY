import requests
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

addresses = []
rents = []
links = []
# URL of the website containing the cards
url = 'https://appbrewery.github.io/Zillow-Clone/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <li> elements that represent cards
cards = soup.find_all('li', class_='ListItem-c11n-8-84-3-StyledListCardWrapper')  # Replace 'card-class' with the actual class name of your cards

# Iterate over each card
for card in cards:
    # Extract data from each card
    property_title = card.find('address').text.replace(" | ", "").replace(", ", "").strip()
    price_tag = card.find('span', class_='PropertyCardWrapper__StyledPriceLine').text.split("+")[0].split("/")[0].replace("$", "").replace(",","").strip()
    property_link = card.find('a', class_='StyledPropertyCardDataArea-anchor')
    link_href = property_link['href']

    addresses.append(property_title)
    rents.append(price_tag)
    links.append(link_href)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(links)):

    driver.get("https://forms.gle/Xd139u1GurP156V76")
    time.sleep(2)

    # Use the xpath to select the "short answer" fields in your Google Form.
    # Note, your xpath might be different if you created a different form.
    address = driver.find_element(by=By.XPATH,
                                  value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    price = driver.find_element(by=By.XPATH,
                                value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(addresses[n])
    price.send_keys(rents[n])
    link.send_keys(links[n])
    submit_button.click()



