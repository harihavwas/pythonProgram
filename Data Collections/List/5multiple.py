def mult5(lst,l):

    # method 1
    """
    nlst=[]
    for i in lst:
        nlst.append(5*i)
    print("New List : ",nlst)
    """

    # method 2 --> comprehension
    nlst=[i*5 for i in lst]
    print("New list : ",nlst)

l=int(input("ENter limit : "))
lst=[]
print('Enter list elements')
for i in range(l):
    lst.append(int(input()))
print("List     : ",lst)
mult5(lst,l)
