# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent

def getSoup(com_code):
    url = 'https://finance.naver.com/item/main.naver?code=' + com_code
    ua = UserAgent()

    headers = {'user-agent' : ua.ie}
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    return soup

def getPrice(com_code):
    soup = getSoup(com_code)
    no_today = soup.select_one("p.no_today")
    # print(no_today)
    price = no_today.select_one("span.blind").get_text()

    return price

def main():
    com_codes = ["030200", "005930", "035720"]
    com_names = ["KT", "삼성전자", "카카오"]

    prices = []
    for code in com_codes:
        price = getPrice(code)
        prices.append(price)

    df = pd.DataFrame({"종목코드" : com_codes, "상장회사" : com_names, "주가" : prices})
    print(df)

if __name__ == "__main__":
    main()