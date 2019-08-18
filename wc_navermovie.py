# wc_navermovie.py

# 파이썬으로 누구나 크롤링 하기 04
# 네이버 영화 순위 페이지 크롤링 하기
# 평촌 아이티 컴퓨터 www.pitca.co.kr
# 작성자: 전대룡

import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

titles = soup.find_all('div', {'class':'tit3'})

# tit3 클래스 추출하기
for idx, one in enumerate(titles):
    print(idx + 1, one)

# tit3 클래스 중 a 태그와 텍스트 추출하기
for idx, one in enumerate(titles):
    link = one.a['href'] # bs4 객체의 태그 검색
    text = one.a['title']
    print(idx + 1, link, text)

# 영화 인기 랭킹 10위 까지 출력해보기
for num in range(10):
    one = titles[num]
    link = one.a['href']
    # 영화제목 앞, 뒤의 화이트 스페이스를 제거한 텍스트 추출
    text = one.text.strip()
    print(num + 1, link, text)