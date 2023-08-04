# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

def main():
    # index.html을 불러와서 BeautifulSoup 객체 초기화
    soup = BeautifulSoup(open("html/index.html", encoding = "utf-8"), "html.parser")
    # print(type(soup))

    # print(soup.title)
    # <title>The Dormouse's story</title>

    # print(soup.title.string)
    # u'The Dormouse's story'

    # soup.title.parent.name
    # u'head'

    # soup.p
    # <p class="title"><b>The Dormouse's story</b></p>

    # soup.p['class']
    # u'title'

    # soup.a
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    # soup.find_all('a')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    # soup.find(id="link3")
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

    # print(soup.find("p").get_text())

    """
    print(soup.select_one('.fakecampus > p').get_text())
    ----------------------------------------------------------------
    fake_str = soup.find('div', class_ = "fakecampus").find_all('p')
    print(fake_str[2].get_text())
    """

if __name__ == "__main__":
    main()