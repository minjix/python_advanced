# 실습문제 2.4.2
# word_list 에 들어있는 문자열 중 첫글자가
# a 인 것만 뽑아서 리스트로 만들기

words = ['apple', 'watch', 'apolo', 'star', 'abocado']

# 리스트 내포 사용 X
result = []
for word in words:
    if word[0] == 'a':
        result.append(word)
print(result)

# 리스트 내포 사용 O
result2 = [word for word in words if word[0] == 'a']
print(result2)