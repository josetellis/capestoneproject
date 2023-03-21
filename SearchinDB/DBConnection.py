import mysql.connector
from CapestoneExceptions.MysqlException import MYSqLError
class DatabaseConnection():
    def __init__(self):
        self.cur = None

    def Connect(self,localhost,username,password,database,port):
        self.hostname=localhost
        self.username=username
        self.password=password
        self.database=database
        self.portnum=port

        self.connect=mysql.connector.Connect(host=self.hostname,username=self.username,password=self.password,database=self.database,port=self.portnum)
        self.cur=self.connect.cursor()
