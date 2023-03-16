!pip install requests
!pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests 

def extract_content(url, soup): 
	return { 
		"url": url, 
		"title": soup.title.string, 
		"text": soup.find('div',attrs={'data-anchor':'Text'}).text, 
	}

articles = []

urls = ['https://www.scielo.br/j/resr/a/45Gpz8DYsGc48rPJwsM35rm/?lang=en',
        'https://www.scielo.br/j/rceres/a/g7g7rLqtD4ZWvsGjFwknpdn/?lang=en',
        'https://www.scielo.br/j/cagro/a/w5zWctmnVgRfBYVy3nnHXXS/?lang=en',
        'https://www.scielo.br/j/ambiagua/a/zmyKD7KcSpPXfQDFn7cQzLs/?lang=en']
for url in urls:
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  articles.append(extract_content(url,soup))
for article in articles:
 print(article)

