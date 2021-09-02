# import re
# c=0
# m=re.finditer('ab','abaabbab')
# for i in m:
#     c+=1
# print(c)


# import re
# c=0
# m=re.finditer('ab','abaabbab')
# for i in m:
#     print("Match available at : ",i.start())
#     print("Group : ",i.group())
#     c+=1
# print(c)


# import re
# x='[abc]'
# m=re.finditer(x,'abt c05kzabc')
# for i in m:
#     print(i.start())
#     print(i.group())
#
# import re
# x='[^abc]'
# m=re.finditer(x,'abt c05kzabc')
# for i in m:
#     print(i.start())
#     print(i.group())
#
import re
x='[a-z]'
m=re.finditer(x,'abt c05kzabc')
for i in m:
    print(i.start())
    print(i.group())