import bs4
import requests
from textblob import TextBlob
import sqlite3

conn = sqlite3.connect('scraperarticle.db')
c = conn.cursor()





url = 'https://lematin.ma/'

source = requests.get(url).text
soup = bs4.BeautifulSoup(source, 'html.parser')

def scraper_mblock(article_block):
    article_data = {}
    
    try:
        article_data['title'] = article_block.find('a', {'class': 'article-title'}).get_text()
    except AttributeError:
        article_data['title'] = None
        
    try:
        article_data['content'] = article_block.find('a', {'class': 'article-body'}).get_text()
    except AttributeError:
        article_data['content'] = None
        
    try:
        article_data['image'] = article_block.find('img', {'class': 'lazy'}).get('data-src')
    except AttributeError:
        article_data['image'] = None
    
    return article_data

def scrape_a_page(article_blocks):
    articles_page_data = []
    
    for article_block in article_blocks:
        articles_page_data.append(scraper_mblock(article_block))
    
    return articles_page_data

articles_blocks = soup.findAll('div', {'class': 'article'})
data = scrape_a_page(articles_blocks)

for article in data:
    print("Title:", article['title'])
    
    if article['content'] is not None:
        blob = TextBlob(article['content'])
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = "positif"
        elif polarity < 0:
            sentiment = "négatif"
        else:
            sentiment = "neutre"
    else:
        sentiment = 'None'

    c.execute('''INSERT INTO articles VALUES(?, ?, ?, ?)''', (article['title'], article['content'], article['image'], sentiment))

conn.commit()
print('data store with successfully')

c.execute('SELECT * FROM articles')
data = c.fetchall()

conn.close()