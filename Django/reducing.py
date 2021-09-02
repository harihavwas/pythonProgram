from functools import reduce
lst=[2,3,4,5]
total=reduce(lambda num1,num2:num1+num2,lst)
print(total)

largest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(largest)

smallest=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(smallest)
