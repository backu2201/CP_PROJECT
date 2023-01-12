from time import perf_counter,sleep
from threading import Thread
import os
class Search:
    def task(self,n,t):
        a=False
        sleep(1)
        for r, d, f in os.walk(t):
            for j in f:
                if j == n:

                    a=True
                    break
        if a:
            print("file is found")
        else:
            print("file is not found")
if __name__ == "__main__":
    s=Search()

    t1 = Thread(target=s.task, args=("MT1.txt", "c:\\"))
    t2 = Thread(target=s.task, args=("MT1.txt", "c:\\HCL"))
    start_time = perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = perf_counter()
    print(f'{end_time - start_time}seconds')




