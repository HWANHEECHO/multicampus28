# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

def createDF(result_list):
    result_df = pd.DataFrame({"title" : result_list})
    return result_df

def crawler(soup):
    # print(soup)
    tbody = soup.find("tbody")

    result = []
    for p in tbody.find_all("p", class_ = "title"):
        result.append(p.get_text().replace('\n', ''))

    return result

def main():
    url = "https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01"
    custom_header = {
        'referer' : 'https://music.bugs.co.kr/',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    req = requests.get(url, headers = custom_header)
    print(req.status_code)
    # print(req.text)
    soup = BeautifulSoup(req.text, "html.parser")
    result = crawler(soup)
    df = createDF(result)
    print(df)
    df.to_csv('result.csv', index = False)

if __name__ == "__main__":
    main()