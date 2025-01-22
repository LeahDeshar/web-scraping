from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.bbc.com/news'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h2', {'data-testid': 'card-headline'})
    for headline in headlines:
        print(headline.text.strip())
        
    descriptions = soup.find_all('p', {'data-testid': 'card-description'})
    for desc in descriptions:
        print(desc.text.strip())
        
    links = soup.find_all('a', {'data-testid': 'internal-link'})
    for link in links:
        print(link.get('href'))
        
    time_upload = soup.find_all('span', {'data-testid': 'card-metadata-lastupdated'})
    for time in time_upload:
        print(time.text.strip())
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = [headline.text.strip() for headline in soup.find_all('h2', {'data-testid': 'card-headline'})]
    descriptions = [desc.text.strip() for desc in soup.find_all('p', {'data-testid': 'card-description'})]
    links = [link.get('href') for link in soup.find_all('a', {'data-testid': 'internal-link'})]
    time_upload = [time.text.strip() for time in soup.find_all('span', {'data-testid': 'card-metadata-lastupdated'})]
    
    min_length = min(len(headlines), len(descriptions), len(links), len(time_upload))
    
    headlines = headlines[:min_length]
    descriptions = descriptions[:min_length]
    links = links[:min_length]
    time_upload = time_upload[:min_length]
    
    data = {
        'Headline': headlines,
        'Description': descriptions,
        'Link': links,
        'Time Uploaded': time_upload
    }
    df = pd.DataFrame(data)
    
    df.to_csv('scraped_data.csv', index=False)
    print("Data saved to scraped_data.csv")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")