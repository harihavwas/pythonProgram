# a=input("Enter a string")
# # p=0
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if (a[i]==a[j]):
#             print(a[i])
#             exit()
#     # if (p!=0):
#     #     print(a[p])
#     #     break
#
#


a=input("Enter a string")
b=""
for i in a:
    if i not in b:
        b=b+i
    else:
        print(i)
        break