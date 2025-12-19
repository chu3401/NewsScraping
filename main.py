# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 10:39:08 2025

@author: C
"""

from scraper import NewsScraper

if __name__ == "__main__":
    search_list = ['中鋼']
    scraper = NewsScraper(search_list)
    scraper.fetchNews()
    scraper.saveCsv()