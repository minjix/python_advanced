# 모듈 추가
import sqlite3

# 데이터 베이스 열기
conn = sqlite3.connect('myvenv/Chapter05/sql_ddl.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령어 작성
UPDATE_SQL = "UPDATE item SET price = 650000 WHERE code = 'A00002';"

# SQL 명령 실행
cur.execute(UPDATE_SQL)

# 커밋 : insert, update, delete 는 커밋을 해야 실제로 반영됨
conn.commit()

# 데이터베이스 닫기
conn.close()