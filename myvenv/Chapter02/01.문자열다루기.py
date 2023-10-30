# 1. replace
# 문자열 교체 메소드
a = '오늘 날씨는 흐림입니다.'.replace('흐림', '맑음')
print(a)

# 2. find
# 문자열 찾기
b = 'Hello world'.find('world')
print(b)

# 3. split
# 문자열 분리
c = '나이키신발 265 x1212 78000'.split()
print(c)

c2 = '나이키신발,265,x1212,78000'.split(',')
print(c2)

# 4.  strip
# 문자열 공백 제거
d = '     Yeah     '.lstrip()
print(d)
e = '     Yeah     '.rstrip()
print(e)
f = '     Yeah     '.strip()
print(f)