from time import perf_counter,sleep

import os
import multiprocessing as mp
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
    p1=mp.Process(target=s.task,args=("PC1.txt","c:\\"))
    p2=mp.Process(target=s.task,args=("PC1.txt","c:\\MTI"))
    start_time=perf_counter()
    p1.start()
    p2.start()
    end_time=perf_counter()
    print(f'{end_time - start_time}seconds')
