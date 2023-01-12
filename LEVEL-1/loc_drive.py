import win32api
class B:

    def getdrives(self):
        drives=win32api.GetLogicalDriveStrings()
        drives=drives.split('\000')[:-1]
        return drives
r=B()
print(r.getdrives())