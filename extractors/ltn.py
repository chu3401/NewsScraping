# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 10:44:26 2025

@author: C
"""

from bs4 import BeautifulSoup


def extract(soup: BeautifulSoup) -> str:
    try:
        div = soup.find('div', class_="text")
        if not div:
            return ""

        paragraphs = div.find_all('p', class_='')
        content = ''.join(p.get_text() for p in paragraphs)

        return (
            content.replace('\r', ' ')
                   .replace('\n', ' ')
                   .replace('\xa0', ' ')
                   .replace('一手掌握經濟脈動', '')
                   .replace('點我訂閱自由財經Youtube頻道', '')
        )
    except Exception:
        return ""
