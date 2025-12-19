# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:30:43 2025

@author: C
"""

from bs4 import BeautifulSoup

def extract(soup: BeautifulSoup) -> str:
    try:
        section = soup.find('div', class_="col-11 py-3 div_Article_Info")
        if not section:
            return ""

        paragraphs = section.find_all('p')
        content = ''.join(p.get_text() for p in paragraphs)
        return content.replace('\r', ' ').replace('\n', ' ')
    except Exception:
        return ""

'''   
if domain == 'www.moneyweekly.com.tw':
    
    # 理財周刊
    article_div = soup.find('div', class_="col-11 py-3 div_Article_Info")
    item = article_div.find_all('p')
    content = [elem.get_text() for elem in item]
    content = [elem for elem in content]
    content = ''.join(content)
    content = content.replace('\r', ' ').replace('\n', ' ')
'''