import os
import threading
from task5__6_db import SearchDB
import logging
from task5_log import searchLog

class FileSearcher(threading.Thread):
    drive=""
    file_name=""
    def __init__(self):
        pass
    def search_for_file(self,drive ,file_name):
        try:
            print("This is a search method for file searcher")
            file_paths=[]
            drv=drive+":\\"
            print(drv)
            for r,d,f in os.walk(drv):
                for name in f:
                    if name==file_name:
                        path=os.path.abspath(os.path.join(r,name))
                        file_paths.append(path)
                        self.search_for_file(self, drive ,file_name)


        except:
            #print("there is no error")
            pass

        return  file_paths

    def run(self):
        self.search_for_file(self.drive,self.file_name)
if __name__=='__main__':
    data=[]
    drive = input("enter the drive:")
    file_name = input("enter the file name:")
    obj=FileSearcher()

    dbobj=SearchDB()
    searchLg=searchLog()
    res = dbobj.searchDB(file_name)
    if res==0:
        data = obj.search_for_file(drive , file_name)
        try:
            print(data[0])
            dbobj.insertDB(data[0])
            logging.info(data[0])
        except IndexError:
            # print("No such file exsists")
            logging.info("no such file exsists")

        else:
            print(res)