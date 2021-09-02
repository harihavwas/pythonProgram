x=5
def fun():
    x=3
    #global x
    x+=10
    print("Local : ",x)
fun()
print("Global : ",x)