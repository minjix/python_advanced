# 시간을 분으로 변경

# str_time = input("시간을 입력하세요>>>")

# total = 0
# list_time = str_time.split()
# if len(list_time) > 1:
#     time = int(list_time[0].split('시간')[0])
#     bun = int(list_time[1].split('분')[0])
#     total = time * 60 + bun
# else:
#     if list_time[0].find('시간') > 0:
#         total = int(list_time[0].split('시간')[0])*60
#     else:
#         total = int(list_time[0].split('분')[0])

# print(total)


# ------------------- 풀이 해준것
time2 = input("시간을 입력하세요>>>")

# 1. 분만 있는 경우
# 2. 시간만 있는 경우
# 3. 시간과 분이 있는 경우

if time2.find('시간') == -1:
    # 분만 있는 경우
    result = int(time2.split('분')[0])
else:
    if time2.find('분') == -1:
        # 시간만 있는 경우
        result = int(time2.split('시간')[0])*60
    else:
        # 시간과 분이 있는 경우
        sub = time2.split('시간')
        result = int(sub[0])*60 + int(sub[1].split('분')[0])
print(result)