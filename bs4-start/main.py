from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text #just like reading the file

soup = BeautifulSoup(yc_web_page,"html.parser")

#article_tag = soup.find(name="a",class_="titlelink")
#article_text = article_tag.getText()
#article_link = article_tag.get('href')
#article_upvote = soup.find(name='span',class_='score').getText() #getting the ratings

articles = soup.find_all(name="a",class_="titlelink")
articles_texts = []
articles_links = []
for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get('href')
    articles_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span',class_='score')]

largest_value= max(article_upvotes)

largest_index = article_upvotes.index(largest_value)

print(articles_texts[largest_index])
print(articles_links[largest_index])
print(article_upvotes [largest_index])

# print(articles_texts)
# print(articles_links)
# print(article_upvotes)



#article_score = article_upvote.getText()
#print(article_text)
#print(article_link)
#print(article_upvote)

































#import lxml

# with open("website.html",encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# #print(soup.title)
# #print(soup.title.name)
# #print(soup) prettify()
# #print(soup.a) #anchor tag
#
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
#
# for tag in all_anchor_tags: #websites in tags
#     #print(tag.getText())
#     print(tag.get('href'))
#
# heading = soup.find(name='h1',id='name')
# print(heading)
#
# section = soup.find(name='h3',class_='heading')
# print(section) #getText(), .name
#
# compny_url = soup.select_one(selector="p a")
# print(compny_url)
#
# name = soup.select_one(selector='#name')
# print(name)