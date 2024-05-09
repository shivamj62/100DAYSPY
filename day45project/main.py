import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

allmovies=soup.find_all(name="h3", class_="title")
movie_title = [movie.get_text() for movie in allmovies]
movie = movie_title[::-1]


with open("movies.txt", mode="w",encoding="utf-8") as file:
    for mv in movie:
        file.write(f"{mv}\n")





