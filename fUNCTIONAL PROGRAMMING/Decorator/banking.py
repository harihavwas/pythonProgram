def admin_req(func):
    def wrapper(a,b):
        if a!='admin':
            raise Exception("You are not allowewd !")
        else:
            return func(a,b)
    return wrapper

@admin_req
def change_pin(user,pin):
    mpin=pin
    return pin

@admin_req
def del_acc(user,pin):
    return str(accn)+" Delete"

print(change_pin("admin",1000))
print(del_acc("Hari",4268))