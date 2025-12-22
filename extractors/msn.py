# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:34:16 2025

@author: C
"""

from bs4 import BeautifulSoup

def extract(soup: BeautifulSoup) -> str:
    try:
        main = soup.find('div', class_='consumption-feed-content ')
        if not main:
            return ""

        sections = main.find_all('section')
        content = []

        for section in sections:
            paragraphs = section.find_all('p')
            for p in paragraphs:
                text = p.get_text(strip=True)
                if text:
                    content.append(text)

        return (
            ''.join(content)
            .replace('\r', ' ')
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