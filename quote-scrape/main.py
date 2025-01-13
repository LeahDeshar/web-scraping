from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = 'https://quotes.toscrape.com/page/{}/'  
quote_list = []

for page in range(1, 11):  
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    tags = soup.find_all('div', class_='tags')

    for i in range(len(quotes)):
        tag_list = [tag.text.strip() for tag in tags[i].find_all('a', class_='tag')]
        tag_str = ', '.join(tag_list)  
        
        quote_list.append([quotes[i].text.strip(), authors[i].text.strip(), tag_str])

df = pd.DataFrame(quote_list, columns=['Quote', 'Author', 'Tags'])

file_name = 'quotes.csv'
df.to_csv(file_name, index=False)

print(f"Scraped {len(df)} quotes and saved to '{file_name}'")
