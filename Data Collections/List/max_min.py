# MAXIMUM AND MINIMUM

def max_min(lst,l):
    """
    min=lst[0]
    maxi=lst[0]
    for i in lst:
        if min>i:
            min=i
        if maxi<i:
            maxi=i
    print("Minimum : ",min,"\nMaximum : ",maxi)
"""
    """
    for i in range(l):
        for j in range(i + 1, l):
            if (lst[i] > lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    print("Minimum : ",lst[0],"Maximum : ",lst[-1])
    """
l=int(input("ENter limit : "))
lst=[]
print('Enter list elements')
for i in range(l):
    lst.append(int(input()))

max_min(lst,l)