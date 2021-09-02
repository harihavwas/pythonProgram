

# Print even numbers from list
lst=[2,5,7]
# def even(num):
#     return num%2==0
evens=list(filter(lambda num:num%2==0,lst))
print(evens)

# Print odd numbers
odds=list(filter(lambda num:num%2!=0,lst))
print(odds)

def odd(num):
    return num%2!=0
oddss=list(filter(odd,lst))
print(oddss)