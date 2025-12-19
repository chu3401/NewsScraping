# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 15:42:38 2025

@author: C
"""

import re
from bs4 import BeautifulSoup

def extract(soup: BeautifulSoup) -> str:
    try:
        scripts = soup.find_all('script')
        if len(scripts) < 2:
            return ""

        raw = str(scripts[-2])

        if 'ReactDOM.render' not in raw:
            return ""

        content = raw.split('ReactDOM.render(React.createElement(')[1]
        content = content.split(',')[1]
        content = content.replace('{"content":"', '').replace('"})', '')

        content = re.sub(r'\\u003[a-z]+', '', content)
        content = content.replace('/p', ' ').replace('\\n', '')

        return content
    except Exception:
        return ""

'''
if domain == 'fnc.ebc.net.tw':

    # EBC東森財經新聞
    content = str(soup.find_all('script')[-2]).split('ReactDOM.render(React.createElement(')[1]
    content = content.split(',')[1].replace('{"content":"', '').replace('"})', '')
    content = re.sub(u'\\\\u003[a-z]+', '', content)
    content = content.replace('/p', ' ').replace('\\n', '')
'''
