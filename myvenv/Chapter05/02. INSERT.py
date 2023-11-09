# 모듈 추가
import sqlite3

# 데이터 베이스 열기
conn = sqlite3.connect('myvenv/Chapter05/sql_ddl.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령어 작성
INSERT_SQL = "INSERT INTO item(code, name, price) VALUES(? ,? ,?);"

# 데이터 여러개 한번에 추가하기
data = (
    ('A00002', '에어컨 20평형', 350000),
    ('A00003', '최신형 스마트폰', 800000),
    ('A00004', '가성비 노트북', 650000)
)

# SQL 명령 실행
cur.executemany(INSERT_SQL, data)

# 커밋 : insert, update, delete 는 커밋을 해야 실제로 반영됨
conn.commit()

# 데이터베이스 닫기
conn.close()