# wc_nmovie.py

# 파이썬으로 누구나 크롤링 하기 06
# 네이버 웹툰 크롤링
# 평촌 아이티 컴퓨터 www.pitca.co.kr
# 작성자: 전대룡

# https://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue&page=2

import webbrowser
import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue&page='
pagenum = 0

while True:
    pagenum += 1
    url = url + str(pagenum)
    resp = requests.get(url)
    if resp.status_code != 200:
        break

    soup = BeautifulSoup(resp.text, 'html.parser')
    wtoon = soup.find('table', {'class':'viewList'})
    wtoon_title = wtoon.find_all('td', {'class':'title'})

    html = ''
    for one in wtoon_title:
        linkURL = 'https://comic.naver.com/' + one.a['href']
        linkText = '<a href = "%s">%s</a>' % (linkURL, one.text.strip())
        print(linkText + "<br>")
