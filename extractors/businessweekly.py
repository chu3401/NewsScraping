# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 10:44:26 2025

@author: C
"""

from bs4 import BeautifulSoup


def extract(soup: BeautifulSoup) -> str:
    try:
        section = soup.find('div', class_='article_main')
        if not section:
            return ""

        paragraphs = section.find_all('p')
        content = ''.join(p.get_text() for p in paragraphs)
        return content.replace('\r', ' ').replace('\n', ' ')
    except Exception:
        return ""