# 1. 위치 가변 매개변수
def print_fruits(*args):
    for arg in args:
        print(arg)

print_fruits('apple', 'orange', 'mango', 'grape')

# 2. 키워드 가변 매개변수
def coment_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

coment_info(name= '파린이', content='Thanks')

# 매개변수 작성 순서
# 위치 - 가변 - 위치 가변 - 키워드(기본) - 키워드 가변
def post_info(*tags, title, content):
    print(f'제목:{title}')
    print(f'내용:{content}')
    print(f'태그:{tags}')

post_info('#파이썬', '#함수', title = '제목이다', content = '내용이다')