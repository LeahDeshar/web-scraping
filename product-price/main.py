from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.amazon.com/s?k=women+footwear&rh=p_36%3A-5000&_encoding=UTF8&content-id=amzn1.sym.3a233c37-ffc8-403c-b9df-0a8759916b7a&crid=1ZVS48U85MWPY&pd_rd_r=2e021792-9f0f-405e-95f1-dd4b68eb7684&pd_rd_w=pyW0e&pd_rd_wg=7u1rH&pf_rd_p=3a233c37-ffc8-403c-b9df-0a8759916b7a&pf_rd_r=9ATQAZQP3XC67W9EC850&qid=1663550577&rnid=2661611011&sprefix=Women+Footw%2Caps%2C286&ref=pd_hp_mw_btf_unk'

response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') 
    titles = soup.find_all('span')
    
    print(titles)
    
    for title in titles:
        print("Titles")
        print(title.text.strip())