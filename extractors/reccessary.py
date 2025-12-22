# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:34:16 2025

@author: C
"""

from bs4 import BeautifulSoup

def extract(soup: BeautifulSoup) -> str:
    try:
        main = soup.find('div', class_='pg-col-wrap grid-h')
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
