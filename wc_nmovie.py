# wc_nmovie.py

# 파이썬으로 누구나 크롤링 하기 05
# 일자별 네이버 영화 순위 크롤링 하여 페이지 만들기
# 평촌 아이티 컴퓨터 www.pitca.co.kr
# 작성자: 전대룡

import requests
from bs4 import BeautifulSoup

# 특정 일자 영화 순위 URL 생성하기
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&tg=0&date=20190816'
date = input('언제 영화 순위를 검색할까요? (yyyymmdd): ')

response = requests.get(url + date)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('div', {'class':'tit3'})

for one in titles:
    linkURL = 'https://movie.naver.com/' + one.a['href']
    linkText = '<a href = "%s">%s</a>'%(linkURL, one.a['title'])
    print(linkText)