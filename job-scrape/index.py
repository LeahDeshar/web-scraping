

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import time

BASE_URL = 'https://www.indeed.com/jobs?q=software+developer&l='

def fetch_job_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    for job_card in soup.find_all('div', class_='job_seen_beacon'):
        title = job_card.find('h2', class_='jobTitle').get_text(strip=True)
        company = job_card.find('span', class_='companyName').get_text(strip=True)
        location = job_card.find('div', class_='companyLocation').get_text(strip=True)
        description = job_card.find('div', class_='job-snippet').get_text(strip=True)

        job_type = job_card.find('div', class_='jobCardShelfItem').get_text(strip=True) if job_card.find('div', class_='jobCardShelfItem') else 'N/A'

        jobs.append([title, company, location, description, job_type])

    return jobs

def collect_job_listings():
    all_jobs = []
    for page in range(1, 6):  
        url = f'{BASE_URL}&start={page * 10}'  
        jobs = fetch_job_listings(url)
        all_jobs.extend(jobs)
        
        time.sleep(2)

    return all_jobs

def save_to_csv(jobs):
    df = pd.DataFrame(jobs, columns=['Job Title', 'Company', 'Location', 'Description', 'Job Type'])
    df.to_csv('job_listings.csv', index=False)
    print("Job listings saved to job_listings.csv")

def save_to_db(jobs):
    conn = sqlite3.connect('job_listings.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            job_type TEXT
        )
    ''')

    cursor.executemany('''
        INSERT INTO jobs (title, company, location, description, job_type)
        VALUES (?, ?, ?, ?, ?)
    ''', jobs)

    conn.commit()
    conn.close()
    print("Job listings saved to job_listings.db")

def main():
    jobs = collect_job_listings()
    
    save_to_csv(jobs)
    


if __name__ == '__main__':
    main()
