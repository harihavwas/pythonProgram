'''
map(function,argument)
'''


lst=[2,5,7]
# def sqr(num):
#     return num**2
# print(list(map(sqr,lst)))

cube=list(map(lambda num:num**3,lst))
print(cube)

sqr=list(map(lambda n:n**2,lst))
print(sqr)