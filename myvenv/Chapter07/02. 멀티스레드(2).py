import threading
import time

# 주식 자동매매
# 매수 ,매도

# 매수 스레드
def buyer():
    for i in range(5):
        print("[매수] 데이터 요청 중...")
        time.sleep(1)
        print("[매수] 데이터 분석 중...")
        time.sleep(1)
        print("[매수] 메수 타이밍!!...")
        time.sleep(1)
        print("[매수] 매수!!...")
        time.sleep(1)

# 매도 스레드
def seller():
    for i in range(5):
        print("[매도] 데이터 요청 중...")
        time.sleep(1)
        print("[매도] 데이터 분석 중...")
        time.sleep(1)
        print("[매도] 매도 타이밍??...")
        time.sleep(1)
        print("[매도] 매도 실패!!...")
        time.sleep(1)

# 메인 스레드
print("[main] start")
buyer = threading.Thread(target=buyer)
seller = threading.Thread(target=seller)

buyer.start()
seller.start()

buyer.join() # 매수 스레드가 종료될 때까지 메인 스레드가 대기
seller.join() # 매도 스레드가 종료될 때까지 메인 스레드가 대기
print("[main] 장이 종료 되었습니다.")
