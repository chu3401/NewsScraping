# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:34:16 2025

@author: C
"""

from bs4 import BeautifulSoup

def extract(soup: BeautifulSoup) -> str:
    try:
        sections = soup.find('section', style='margin-top:30px')
        content=[]
        
        for section in sections:
            p_tag = section.find('p')
            if p_tag:
                content.append(p_tag.get_text())

        content = ''.join(content)
        
        return (
            content.replace('\r', ' ')
                   .replace('\n', ' ')
                   .replace('\xa0', ' ')
        )
    except Exception:
        return ""

"""
if domain == 'news.cnyes.com':

    # 鉅亨網
    sections = soup.find_all('section', style='margin-top:30px')
    content = list()
    for section in sections:
        p_tag = section.find('p')
        if p_tag:
            content.append(p_tag.getText())
    content = ''.join(content)
    content = content.replace('\r', ' ').replace('\n', ' ').replace(u'\xa0', ' ')
"""