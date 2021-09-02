"""

1. Class     --> Design patern
2. Object    --> Real world entity
3. Reference --> Operations

"""

# Class
class Person:
    def walk(self): #instance keyword
        print("Person is walking")
    def read(self):
        print("Person is reading")

# Object 1
pe=Person()
pe.walk()
pe.read()

# Object 2
pe1=Person()
pe1.walk()
pe1.read()