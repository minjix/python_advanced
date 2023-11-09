from multiprocessing import Process
import time

class SubProcess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")

if __name__ == "__main__":
    print("[main] start")
    p = SubProcess(name='startcoding')
    p.start()
    time.sleep(1)
    # 프로세스가 살아있는지 검사
    #print(p.is_alive())
    if p.is_alive():
        p.terminate()
    print("[main] end")

    # 추가함수
    # 1. 스레드가 데이터 처리(lock)
    # 2. 프로세스간 데이터 전송(Que, Pipe)
    # 3. 속도 비교
    # 4. 운영체제와 메모리