import sqlite3
class SearchDB():
    def __init__(self):
        self.connect=sqlite3.connect("c://sqlite//hcl.db")
        self.cur = self.connect.cursor()

    def searchDB(self,fil):

        sql="""select * from filelog where filename like '%{0}'""".format(fil)
        self.cur.execute(sql)
        row=self.cur.fetchone()
        if row == None:
            return 0
        else:
            return row

    def insertDB(self,filename):
        sql=""" insert into filelog(filename) values(?);"""
        data=(filename,)
        self.cur.execute(sql,data)
        self.connect.commit()
        return "Record Added"
# if __name__=='__main__':
#     filename=input("enter filename:")
#     obj=SearchDB()
#     print(obj.searchDB(filename))


