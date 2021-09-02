def age_limit(func):
    def wrapper(a,b,c):
        if b<18:
            raise Exception("Not eligible for vaccine !")
        else:
            return func(a,b,c)
    return wrapper

@age_limit
def apply(name,age,place):
    return "Completed"
print(apply("Hari",19,"Polp"))
