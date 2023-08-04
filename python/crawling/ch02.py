# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

def crawler(soup):
    # print(soup)
    div = soup.find("div", class_ = "list_body")

    result = []
    for a in div.find_all("a"):
        result.append(a.get_text())

    return result

def main():
    # 요청 url 변수에 담긴 url의 html 문서를 출력한다.
    """
    url = "https://www.naver.com"
    req = requests.get(url)
    print(req.status_code)
    """

    # 연합뉴스 뉴스 제목 타이틀 가져오기
    url = "https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y"
    custom_header = {
        'referer' : 'https://www.naver.com',
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    req = requests.get(url, headers = custom_header)
    print(req.status_code)
    # print(req.text)
    soup = BeautifulSoup(req.text, "html.parser")
    result = crawler(soup)
    print(result)

if __name__ == "__main__":
    main()