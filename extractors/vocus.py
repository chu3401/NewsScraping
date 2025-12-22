# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:30:43 2025

@author: C
"""

from bs4 import BeautifulSoup

CANDIDATE_CONTAINERS = [
    ('section', {'id': 'article_body'}),
    ('div', {'class': 'article-layout-wrapper'}),
    ('div', {'class': 'main-content'}),
    ('main', {'id': 'article-container'}),
]

def extract(soup: BeautifulSoup) -> str:
    try:
        container = None

        for tag, attrs in CANDIDATE_CONTAINERS:
            container = soup.find(tag, attrs)
            if container:
                break

        if not container:
            return ""

        paragraphs = container.find_all(['p','span'])
        content = ''.join(
            p.get_text(strip=True)
            for p in paragraphs
            if p.get_text(strip=True)
        )

        return (
            content
            .replace('\r', ' ')
            .replace('\n', ' ')
            .replace('\xa0', ' ')
        )
    except Exception:
        return ""

'''   
if domain == 'www.cmoney.tw':

    # CMoney 投資網誌 
    item = soup.find_all('div', itemprop="articleBody")[0].find_all('p')
    content = [elem.getText() for elem in item]
    content = [elem for elem in content]
    content = ''.join(content)
    content = content.replace('\r', ' ').replace('\n', ' ')
'''