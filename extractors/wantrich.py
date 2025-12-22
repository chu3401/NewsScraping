# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 10:43:49 2025

@author: C
"""

from bs4 import BeautifulSoup


def extract(soup: BeautifulSoup) -> str:
    try:
        section = soup.find('div', class_='article-wrapper')
        if not section:
            return ""

        paragraphs = section.find_all('p')
        content = ''.join(p.get_text() for p in paragraphs)
        return content.replace('\r', ' ').replace('\n', ' ')
    except Exception:
        return ""