# l=int(input("Enter limit"))
# for i in range(l+1):
#     for j in range(i):
#         print("*",end="")
#     print("")

# l=int(input("Enter limit"))
# for i in range(l,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("")


# n=int(input("Enter limit : "))
#
# def pattern(n):
#     k=1
#     for i in range (1,n+1):
#         for j in range(1,i):
#             print(k,end=" ")
#             k+=1
#         print("\r")
#
# pattern(n)


# def pattern(n):
#     for i in range (1,n+1):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print("\r")
# n=int(input("Enter limit : "))
# pattern(n)


# n=int(input("Enter limit : "))

# def pattern(n):
#     for i in range (1,n+1):
#         for j in range(1,n+1):
#             print("*",end=" ")
#         print("\r")
#
# pattern(n)

def pattern(n):
    q=n+1
    for i in range (n):
        for j in range(q):
            print(end=" ")
        q+=1
        for r in range (n):
            print("*",end=" ")
        print("\r")
n=int(input("Enter limit : "))
pattern(n)