# 실습문제 6.1.1
# 날짜 형식 검사하기

# YYYY/MM/DD 형식으로표현된 날짜를 검사하는 정규표현식 만들기
# 1. 연도는 4자리 숫자로 표현한다(1000~9999)
# 2. 달은 1~12월 ,일은 1~31일 까지 표현한다.

# ^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[1|2][0-9]|3[01])$

import re

pattern = '^\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[1|2][0-9]|3[01])$'

datas=[
    '2022/08/08',
    '1000/01/01',
    '9999/12/31',
    '900/02/02',
    '12000/10/26',
    '2021/13/01',
    '2023/2/02',
    '2024/06/3',
    '2023/06/35'
]

for data in datas:
    # result = re.findall(pattern, data)
    # res = ''
    # if len(result) > 0:
    #     res = 'True'
    # else:
    #     res = 'False'
    
    # print(data, res)
    
    matchObj = re.match(pattern, data)
    result = (lambda x : True if x != None else False)(matchObj)

    print(f'{data} {result}')