# FILE OPERATION
"""
1. Read
2. Write
"""
data=None
with open('abc',"r") as f:
    data=f.read()
with open('cba',"w+") as k:
    k.write(data)
    k.seek(0)
    print(k.read())