from bs4 import BeautifulSoup
import requests
import csv

URL = "https://www.scrapethissite.com/pages/simple/"

raw_page = requests.get(URL)

text_page = raw_page.text

soup = BeautifulSoup(text_page,"html.parser")

country_tags = soup.find_all(name = 'h3', class_ = 'country-name')
country_names = [name.getText() for name in country_tags]
country_names = [name.strip() for name in country_names]

detail_tags = soup.find_all(name = 'div', class_ = 'country-info')
country_details = [detail.getText() for detail in detail_tags]
country_details = [detail.strip() for detail in country_details]

country_details = [country.replace('\n',' - ') for country in country_details]

country_list = []

for i in range(len(country_names)):
    x = country_names[i] +' - '+ country_details[i]
    country_list.append(x)

country_list.sort()

#with open("country_list.txt", mode = 'w', encoding="utf-8") as file:
#   for i in country_list:
#       file.write(f"{i}\n")

with open("country_list.csv",mode = 'w', encoding="utf-8") as excel:
    for i in country_list:
        excel.write(f"{i}\n")