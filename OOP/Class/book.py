class Book:
    def libname(self,libname):
        self.libname=libname
        print("Library name : ",self.libname)
    def bkname(self,bkname):
        self.bkname=bkname
        print("Bookname : ",self.bkname)
    def author(self,author):
        self.author=author
        print("Author name : ",self.author)
    def page(self,page):
        self.page=page
        print("Page : ",self.page)
b1=Book()
lib=input("Enter library name : ")
bk=input("Enter Book name : ")
au=input("Enter author name : ")
pg=int(input("Enter pages : "))
b1.libname(lib)
b1.bkname(bk)
b1.author(au)
b1.page(pg)