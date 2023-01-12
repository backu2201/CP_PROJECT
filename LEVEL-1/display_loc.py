import os
import loc_drive as ta
from loc_drive import B
from time import sleep,perf_counter
class Search:
    def search_file(self,n,t):
        k=[]
        for i in t:
            for r,d,f in os.walk(i):
                for j in f:
                    if j==n:
                        print("file is found in {}".format(i))
                        k.append(i)
                        print(r)
                        break
        for i in range(len(t)):
            if t[i] not in k:
                print("file not found in {}".format(t[i]))
if __name__ == "__main__":
    n=input("enter the file name to be searched")
    start_time = perf_counter()
    g=B()

    t=g.getdrives()
    s=Search()
    s.search_file(n,t)
    end_time=perf_counter()
    print(end_time-start_time)

