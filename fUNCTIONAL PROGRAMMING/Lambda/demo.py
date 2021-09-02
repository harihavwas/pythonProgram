# To reduce code
'''
def cb(n):
    print("Result : ",n**3)
n=int(input("Enter number : "))
cb(n)
'''


# Cube
'''
cube=lambda n:n**3
print(cube(5))
'''


# Addition
'''
add=lambda a,b:a+b
print(add(2,3))
'''

# String
'''
str=lambda s:s[0]
print(str(input("Enter String : ")))
'''

#even or not
demo=lambda n:n%2
if(demo(int(input("Enter a number : ")))):print("Odd")
else:print("Even")