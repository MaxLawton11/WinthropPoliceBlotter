from bs4 import BeautifulSoup
import pandas as pd
import requests

URL = 'https://winthroptranscript.com/#/police-blotter/'

def fn(num):
    if isinstance(num, int):
        num = str(num)
    if len(num) == 1:
        return '0' + num
    else:
        return num

def ivu(url):
    try:
        response = requests.get(url, headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" })

        if not response.status_code == 200:
            return False
        
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        entry_titles = soup.find_all('h1', class_='entry-title')
        
        for entry_title in entry_titles:
            if 'Police Blotter' in entry_title.text:
                return True
        return False
        
    except Exception as e:
        return False
    
urls = pd.DataFrame({'date':[], 'url':[]})

for year in range(2009, 2024+1) :
    for month in range(1, 12+1) :
        for day in range(1, 31+1) :
            test_date = f"{year}/{fn(month)}/{fn(day)}"
            test_url = URL.replace('#', test_date)
            if ivu(test_url) :
                print('->', test_url)
                urls.loc[len(urls)] = {'date':test_date, 'url':test_url}
            else :
                print('?>', test_url, end='\r')

print()
print(urls)
urls.to_csv('urls.csv')

def getEvents(url) :
    response = requests.get(url, headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" })

    if not response.status_code == 200:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')
    entry_content_div = soup.find('div', class_='entry-content')

    if not entry_content_div:
        print("No div with class 'entry-content' found.")

    events = []
    for p in entry_content_div.find_all('p'):
        events.append(p.text)
    return events


events = pd.DataFrame({'event':[]})

for index, row in urls.iterrows():
    print('Getting events:', row['date'], '-', row['url'])
    for event in getEvents(row['url']) :
        events.loc[len(events)] = {'event':event}

print(events)
events.to_csv('events.csv')