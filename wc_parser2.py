# wc_parser2.py

# 파이썬으로 누구나 크롤링 하기 02
# 웹 페이지 요청하기 - 함수만들기
# 평촌 아이티 컴퓨터 www.pitca.co.kr
# 작성자: 전대룡

import requests

# URL HTML CODE 획득 함수
def get_html(url):
    html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        html = resp.text
    return html

# 다음 사전 페이지 HTML CODE 얻기
url = "https://dic.daum.net"
hcode = get_html(url)
print(hcode)



