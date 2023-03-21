import  openpyxl as xl
import os


class Searchdrives():
    """
    This module helps to find all drives present in pc
    67 to 91 for ascii value
    chr() to convert ascii value to char
    """
    def __init__(self):
        self.drives=[]
        self.workbook=xl.load_workbook("D://testdata//Testdrives.xlsx")
    def searchmydrives(self)->list:
        for x in range(67,91):
            if os.path.exists(chr(x)+":"):
                self.drives.append(chr(x))
        return  self.drives

dr=Searchdrives()
data=str(dr.searchmydrives())
print(data)
sheet=dr.workbook.active
sheet.cell(row=1,column=1).value=data
dr.workbook.save("D://testdata//Testdrives.xlsx")
dr.workbook.close()


