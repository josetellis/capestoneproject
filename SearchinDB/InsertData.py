from CapestoneExceptions.MysqlException import  MYSqLError
import mysql.connector
from SearchinDB.DBConnection import DatabaseConnection
import re
class InsertRecord(DatabaseConnection):
    def __init__(self):
        self.con=self.Connect("localhost",'root','Aptech@123','myhcl',3306)

    def insert(self,files):
        self.files=files
        self.insertcur=self.connect.cursor()
        for f in self.files:
           sql="insert into fileinfo(filename) values(%s);"
           self.insertcur.execute(sql,(f,))
           self.connect.commit()
        print("Files added Successfully")
# try:
#     iserodbj=InsertRecord()
#     iserodbj.insert()
#
# except mysql.connector.Error as err:
#     raise MYSqLError(f'{err.msg}',err.errno)


