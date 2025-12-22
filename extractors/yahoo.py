# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 10:44:46 2025

@author: C
"""

from bs4 import BeautifulSoup


def extract(soup: BeautifulSoup) -> str:
    try:
        body = None
        for cls in ('caas-body', 'atoms'):
            body = soup.find('div', class_=cls)
            if body:
                break

        if not body:
            return ""

        paragraphs = body.find_all('p')
        links = {a.get_text() for a in body.find_all('a')}

        content = [
            p.get_text()
            for p in paragraphs
            if p.get_text() and p.get_text() not in links
        ]

        return ''.join(content).replace('\r', ' ').replace('\n', ' ').replace('\xa0', ' ')
    except Exception:
        return ""