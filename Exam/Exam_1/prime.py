def prime(min,max):
    sum=0
    for i in range(min,max+1):
        c=0
        for j in range(2,i):
            if i%j==0:
                 c+=1
        if c==0:
            sum+=i
    return sum
re=prime(1,50)
print("Sum of prime numbers between 1-50 : ",re)
