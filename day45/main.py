from bs4 import BeautifulSoup
import requests
from requests import Response
response = requests.get("https://news.ycombinator.com/news")

yc_webpage=response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

span_tag = soup.find('span', class_='titleline')

anchor_tag = span_tag.find('a')
anchor_text = anchor_tag.get_text()

score_tag = soup.find('span', class_="score")
score = score_tag.get_text()
print(score)

