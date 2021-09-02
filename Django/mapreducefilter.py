# 1. Map
# 2. Filter
# 3. Reduce






employees=[
    {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
    {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
    {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
    {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
    {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},

]

# Print employees name
'''
for employee in employees:
    print(employee["e_name"])
'''

# print employee in uppercase
'''
for employee in employees:
    print(employee["e_name"].upper())
'''

# Print employee working as developer
'''
for employee in employees:
    if employee["department"]=="developer" :
        print("developer",employee["e_name"])

#total of salaries
total=0
for employee in employees:
    total+=employee["salary"]
print(total)

'''
#print highest salary


'''
e_name=list(map(lambda employee:employee["e_name"],employees))
print(e_name)

e_name=list(map(lambda employee:employee["e_name"].upper(),employees))
print(e_name)
'''

'''
dev=list(filter(lambda emp:emp["department"]=="developer",employees))
print(dev)
deve=list(map(lambda dev:dev["e_name"],dev))
print(deve)
'''

'''
deve=list(map(lambda dev:dev["e_name"],list(filter(lambda emp:emp["department"]=="developer",employees))))
print(deve)
'''

salary=list(map(lambda emp:emp["salary"],employees))
print(sum(salary)  )