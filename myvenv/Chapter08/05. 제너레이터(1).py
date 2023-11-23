# 제너레이터
# 1. 이터레이터를 만드는 함수

def seasons_generator(*args):
    for arg in args:
        yield arg

g = seasons_generator('spring', 'summer', 'autumn', 'winter')

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

def func():
    print("첫번째 작업 중...")
    yield 1

    print("두번쨰 작업 중...")
    yield 2
    
    print("세번쨰 작업 중...")
    yield 3
    
ge = func()
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)