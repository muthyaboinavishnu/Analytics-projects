from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
website = response.text

soup = BeautifulSoup(website,"html.parser")

title_tag = soup.find_all(name='h3',class_='title')
movie_list = [title.getText() for title in title_tag]
movies = movie_list[::-1] # for n in range(len(movie_list) - 1, -1, -1)

with open("movies.txt",mode = 'w') as file:
    for name in movies:
        file.write(f"{name}\n")

