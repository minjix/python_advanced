# 실습문제 6.1.2
# 이메일 정규 표현식 검사

# 1. 이메일은 ID파트와 host 파트로 나눠짐(ID @ host)
# 2. ID 파트는 영문 대소문자, 숫자, 특수문자(-_)
# 3. host 파트는 영문 대소문자, 숫자, 특수문자(-)
# 4. host 파트는 2개 이상의 도메인을 가질 수 있음

import re

datas = [
    'startcoding@maver.com',
    'start-coding@maver.com',
    'start_coding@maver.co.kr',
    'startcoding@k-mail.com',
    '@maver.com',
    'startcoding?@k-mail.com',
    'startcoding@k-mail',
    'startcoding@maver'
]

regex = re.compile('^[\w-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+$')

for data in datas:
    matchObj = regex.match(data)
    result = (lambda x : True if x!= None  else False)(matchObj)

    print(f'{data} {result}')


