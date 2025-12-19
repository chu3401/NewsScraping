import datetime
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import time
from googlenewsdecoder import new_decoderv1
from extractors import DOMAIN_EXTRACTORS


class NewsScraper:
    def __init__(self,search_list,days_back=10):
        self.search_list=search_list
        self.near_start_date = (datetime.date.today() + datetime.timedelta(days=-days_back)).strftime('%Y-%m-%d')
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
            "Referer": "https://www.ctee.com.tw/",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.stock_news = pd.DataFrame()
        
        self.domain_extractors = DOMAIN_EXTRACTORS

    def arrangeGoogleNews(self,elem):
        return ([elem.find('title').getText(),
                elem.find('link').getText(),
                elem.find('pubDate').getText(),
                BeautifulSoup(elem.find('description').getText(), 'html.parser').find('a').getText(),
                elem.find('source').getText()])
    
    def fetchNews(self):
        
        for i,keyword in enumerate(self.search_list):
            print(f'Searching for:{keyword}, Progress: {i + 1} / {len(self.search_list)}')
            url = f'https://news.google.com/news/rss/search/section/q/{keyword}/?hl=zh-tw&gl=TW&ned=zh-tw_tw'
            response=requests.get(url)
            soup=BeautifulSoup(response.text,'xml')
            items=soup.find_all('item')
            rows = [self.arrangeGoogleNews(elem) for elem in items]

            df = pd.DataFrame(data=rows, columns=['title', 'link', 'pub_date', 'description', 'source'])
            df.insert(0, 'search_time', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), True)
            df.insert(1, 'search_key', keyword, True)
            df['pub_date'] = pd.to_datetime(df['pub_date'])
            df = df[df['pub_date'] >= self.near_start_date]
            df = df.sort_values(['pub_date']).reset_index(drop=True)

            self.downloadArticleContents(df)
            self.stock_news = pd.concat([self.stock_news, df])
    
    def downloadArticleContents(self,df):
        news_urls = []
        contents = []
        for i, link in enumerate(df['link']):
            print(f'Downloading news:{df["search_key"].iloc[0]}, Progress: {i+1} / {len(df["link"])}')
            news_url,content=self.beautifulSoupNews(link)
            news_urls.append(news_url)
            contents.append(content)

        df['newsUrl'] = news_urls
        df['content'] = contents


    def beautifulSoupNews(self,url):       
        # 取得Google跳轉頁面的新聞連結
        newsUrl = new_decoderv1(url)["decoded_url"]
        print("---",newsUrl,"---")
        # 取得該篇新聞連結內容
        try:
            response=self.session.get(newsUrl)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error: {http_err}, url: {newsUrl}")
            return newsUrl,""
        except Exception as e:
            print(f"發生錯誤: {e}，網址: {newsUrl}")
            return newsUrl,""
        
        soup = BeautifulSoup(response.text, 'html.parser') 
        # 判斷url網域做對應文章擷取
        domain = re.findall('https?://[^/]*', newsUrl)[0].replace('http://', '').replace('https://', '')
        content = self.extractByDomain(soup, domain, newsUrl)
        return newsUrl, content

        
    def extractByDomain(self,soup,domain,news_url):
        extractor = self.domain_extractors.get(domain)

        if not extractor:
            print('unknow domain')
            print("url=",news_url)
            return "none"
        return extractor(soup)
    
    
    
    def saveCsv(self, filename='checkData.csv'):
        self.stock_news.to_csv(filename, index=False, encoding='utf-8-sig')

if __name__ == "__main__":
    search_list = ['台積電']
    scraper = NewsScraper(search_list)
    scraper.fetchNews()
    scraper.saveCsv()