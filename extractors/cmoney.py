# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:30:43 2025

@author: C
"""

from bs4 import BeautifulSoup

def extract(soup: BeautifulSoup) -> str:
    try:
        section = soup.find('div', itemprop="articleBody")
        if not section:
            return ""

        paragraphs = section.find_all('p')
        content = ''.join(p.get_text() for p in paragraphs)
        return content.replace('\r', ' ').replace('\n', ' ')
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