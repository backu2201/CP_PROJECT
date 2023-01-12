import os
import threading
class FileSearcher(threading.Thread):
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
            pass


        return  file_paths

    def run(self):
        self.search_for_file(self.drive,self.file_name)
if __name__=='__main__':
    data=[]
    drive = input("enter the drive:")
    file_name = input("enter the file name:")
    obj=FileSearcher()
    data = obj.search_for_file(drive, file_name)
    print(data)