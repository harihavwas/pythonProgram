class Book:
    libname="Library"
    def __init__(self,bname,auth,page):
        self.bname=bname
        self.auth=auth
        self.page=page
    def printt(self):
        print("Library Name : ",Book.libname)
        print("Book name : ",self.bname)
        print("Author : ",self.auth)
        print("Page : ",self.page)


bk=input("Enter Book name : ")
au=input("Enter author name : ")
pg=int(input("Enter pages : "))
b1=Book(bk,au,pg)

b1.printt()