# 실습문제 2.4.2
word_list = ['오메가3', None, '비타민C500', None, '홍삼절편']

# 리스트 내포 사용하기 전
result = []
for i in word_list:
    if i == None:
        i = ''
    result.append(i)
print(result)

# 리스트 내포 사용 후
result2 = [i if i != None else '' for i in word_list]
print(result2)