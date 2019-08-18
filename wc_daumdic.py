#

# 파이썬으로 누구나 크롤링 하기 03
# 다음 사전 크롤링 하기
# 평촌 아이티 컴퓨터 www.pitca.co.kr
# 작성자: 전대룡

import requests
from bs4 import BeautifulSoup

# URL HTML CODE 획득 함수
def get_html(url):
    html = ''
    resp = requests.get(url)
    if resp.status_code == 200:
        html = resp.text
    return html

# 다음 사전 페이지 HTML CODE 얻기
# word = input('찾는 단어를 입력하세요: ')
word = 'python'
url_dic = 'http://alldic.daum.net/search.do?q='
hcode = get_html(url_dic + word)
soup = BeautifulSoup(hcode, 'html.parser')

# print(hcode)
# print("=" * 40)
# print(soup)
# hcode와 soup의 차이는?

# 대표 단어블록을 추출한 뒤 txt_search 클래스를 추출하여 단어 목록 출력
# my_dic = soup.find('div', attrs={'class':'cleanword_type kuek_type'})
my_dic = soup.find('div', {'class':'cleanword_type kuek_type'})
print("=" * 40, "my_dic")
print(my_dic)
print("=" * 40)

word = my_dic.find_all('span', {'class':'txt_search'})
for idx, one in enumerate(word):
    print(idx + 1, one, "\t사전검색: ", one.text)
print("=" * 40)

# list_search 클래스의 ul태그를 모두 추출하여 단어 목록 출력
# my_dic = soup.find_all('ul', class_ = {'list_search'})
# my_dic = soup.find_all('ul', attrs = {'class':'list_search'})
my_dic = soup.find_all('ul', {'class':'list_search'})
word = my_dic[0].find_all('span', {'class':'txt_search'})
for idx, one in enumerate(word):
    print(idx + 1, one, "\t사전검색: ", one.text)
print("=" * 40)

# list_search 클래스의 첫 ul태그를 추출
my_dic = soup.find('ul', {'class':'list_search'})
word = my_dic.find_all('span', {'class':'txt_search'})
for idx, one in enumerate(word):
    print(idx + 1, one, "\t사전검색: ", one.text)
