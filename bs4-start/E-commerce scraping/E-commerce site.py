from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

web_data = requests.get(URL)

web_text = web_data.text

soup = BeautifulSoup(web_text,"html.parser")

prod_info = soup.find_all(name = 'a',class_ = 'title')

prod_name = [name.getText().replace('\n','') for name in prod_info]
prod_link = [link.get('href').replace('\n','') for link in prod_info]

prices = soup.find_all(name = 'h4', class_ = 'pull-right price')
prod_price = [price.getText().replace('\n','') for price in prices]

descs = soup.find_all(name = 'p', class_ = 'description')
prod_desc = [desc.getText().replace('\n','') for desc in descs]

ratings = soup.find_all(name = 'div', class_ = 'ratings')
prod_rating = [rate.getText().replace('\n','') for rate in ratings]

product_df = pd.DataFrame({'Name':prod_name,'Description':prod_desc,'Link':prod_link,'Price':prod_price,'Rating':prod_rating})

product_excel = product_df.to_excel('output.xlsx', sheet_name = 'Laptop details')


