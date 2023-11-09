# 모듈 추가
import sqlite3

# 데이터 베이스 열기
conn = sqlite3.connect('myvenv/Chapter05/sql_ddl.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령어 작성
SELECT_SQL = "SELECT * FROM item limit 2;"

# SQL 명령 실행
cur.execute(SELECT_SQL)

rows = cur.fetchall()
for row in rows:
    print(row)

# 데이터베이스 닫기
conn.close()