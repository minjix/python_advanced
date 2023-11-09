# 모듈 추가
import sqlite3

# 데이터 베이스 열기
conn = sqlite3.connect('Chapter05/sql_ddl.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령어 작성
CREATE_SQL = """
    CREATE TABLE if not exists item(
        id integer primary key autoincrement,
        code text not null,
        name text not null,
        price integer not null
    );
"""
# SQL 명령 실행
cur.execute(CREATE_SQL)

# 데이터베이스 닫기
conn.close()