from bs4 import BeautifulSoup
import pandas as pd
import requests


BASE_URL = "https://www.bbc.com/"

def fetch_news():
    reponse = requests.get(BASE_URL)
    