import os
class Search1:
    def task1(n,t):
        a=False
        for r, d, f in os.walk(t):
            for j in f:
                if j == n:
                    a=True
                    break
        if a:
            print("file is found in {}".format(t))
        else:
            print("file not found in {}".format(t))



