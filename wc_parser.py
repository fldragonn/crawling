# wc_parser.py

# 파이썬으로 누구나 크롤링 하기 01
# 웹 페이지 요청하기
# 평촌 아이티 컴퓨터 www.pitca.co.kr
# 작성자: 전대룡

import requests

# 웹페이지 요청할 URL
url = 'https://dic.daum.net/search.do0?q=python'
response = requests.get(url)

# 응답받은 HTML 코드
html = response.text

# 응답받은 HTML 헤더
header = response.headers

# 응답받은 상태 확인
status = response.status_code
is_ok = response.ok

# 응답받은 페이지 인코딩
encoding = response.encoding

print("header: ", header)
print("status: ", status)
print("is_ok: ", is_ok)
print("encoding: ", encoding)
print("html: ", html)
