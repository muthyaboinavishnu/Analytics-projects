from bs4 import BeautifulSoup
#import lxml

with open("website.html",encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title.name)
#print(soup) prettify()
#print(soup.a) #anchor tag

all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags: #websites in tags
    #print(tag.getText())
    print(tag.get('href'))

heading = soup.find(name='h1',id='name')
print(heading)

section = soup.find(name='h3',class_='heading')
print(section) #getText(), .name

compny_url = soup.select_one(selector="p a")
print(compny_url)

name = soup.select_one(selector='#name')
print(name)