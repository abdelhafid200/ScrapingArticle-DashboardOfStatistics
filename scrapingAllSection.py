import bs4
import requests
from textblob import TextBlob
import sqlite3
import csv

connexion = sqlite3.connect('ArticleScrape.db')
cursor = connexion.cursor()
cursor.execute("DROP TABLE IF EXISTS articles")
cursor.execute('CREATE TABLE IF NOT EXISTS articles (section TEXT, title TEXT, contenu TEXT, image TEXT,link_article TEXT, sentiment TEXT, link_section TEXT, image_section TEXT)')


url = 'https://lematin.ma/'
source = requests.get(url).text
soup = bs4.BeautifulSoup(source, 'html.parser')

section_articles = soup.select('aside .side-nav li')
links = []
images_section = []

for article in section_articles:
    images_section.append(article.img['src'] if article.img else None)

for sec in section_articles:
    link = sec.find('a').get('href')
#    section = sec.find('a').get_text().replace("\n",'')
    links.append(link)

def scraper_mblock(article_block):
    article_data = {}

    try:
        article_data['title'] = article_block.find('a', {'class': 'article-title'}).get_text()
    except AttributeError:
        article_data['title'] = None

    try:
        article_data['lien'] = article_block.find('a', {'class': 'article-title'}).get('href')
    except AttributeError:
        article_data['lien'] = None

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

for link, sec, img in zip(links, section_articles, images_section):
    url2 = link
    source2 = requests.get(url2).text
    soup2 = bs4.BeautifulSoup(source2, 'html.parser')
    articles_blocks = soup2.findAll('div', {'class': 'article'})
    data = scrape_a_page(articles_blocks)
    section = sec.find('a').get_text().replace("\n",'')    
    
    for article in data:
        img2 = 'https://lematin.ma/'+img
        print(img2)
        if article['content'] is not None:
            # print("Content:", article['content'])
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

        if article['image'] is not None:
            article['image'] = 'None'
        cursor.execute('''INSERT INTO articles VALUES(?, ?, ?, ?, ?, ?, ?, ?)''', (section, article['title'], article['content'], article['image'], article['lien'], sentiment, url2, img2))

connexion.commit()
print('data store with successfully')


connexion.close()