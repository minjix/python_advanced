# 일급객체
# - 다음과 같은 특징을 만족하는 객체
# 1. 데이터처럼 사용 가능
# 2. 매게변수에 넘겨줄 수 있음
# 3. 리턴값으로 사용될 수 있음

# 1. 데이터 처럼 사용 가능

# 1) 함수를 변수에 할당 가능
def func(x, y):
    return x+ y

add = func
print(add(3,4))


# 2) 리스트(튜플, 딕셔너리) 할당 가능
def mul(x,y):
    return x*y

def div(x,y):
    return x/y

calculator = [mul, div]
print(calculator[0](5,7))

# 2. 매게변수에 넘겨줄 수 있음
def inputData():
    data = input("데이터 입력>>>")
    return data

def start(func):
    print("입력한 데이터는", func())

start(inputData)

# 3. 리턴값으로 사용 가능
def plusTen(a):
    return a + 10

def func(x):
    return plusTen(x)

print(func(5))