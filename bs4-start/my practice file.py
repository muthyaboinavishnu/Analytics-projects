from bs4 import BeautifulSoup
import requests

response_page = requests.get("https://news.ycombinator.com/front")

text_file = response_page.text

# print(text_file)

soup = BeautifulSoup(text_file,"html.parser")

main_titles = []

class_name = soup.find_all(name = 'tr', class_ = 'athing')
#class_name_text = class_name.getText()
for names in class_name:
    name = names.getText()
    main_titles.append(name)

#print(main_titles)

main_links = []
for links in class_name:
    link = links.get('id')
    main_links.append(link)
print(main_links)


