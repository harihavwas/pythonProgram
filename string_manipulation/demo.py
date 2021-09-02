# for i in "abcd":
#     print(i)


#
# a="abcd"
# b="acfg"
# for i in a:
#     if i not in b:
#         print(i)



#
# a="abcd"
# b=a
# print(b)
#
# a="luminar"
# b=""
# for i in a:
#     b=b+i
# print(b)




# a="luminar"
# b=input("Enter element : ")
# if b in a:
#     print("Present")
# else:
#     print("Not present")

# c=0
# a="malayalam"
# n=input("Enter element : ")
# for i in a:
#     if i in n:
#         c=c+1
# print(c)



#
#
# n=input("Enter a string")
#
# for j in n:
#     for i in "abcdefghijklmnopqrstuvwxyz":
#         if j==i:
#             print(i)




n=input("Enter a string")
p="!@#$%^&*()_{}[]:;'|\<,>.?/~`'"
new=""
for i in n:
    if i not in p:
        #print(i)
        new+=i
print(new)