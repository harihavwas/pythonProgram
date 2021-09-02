#  Single Inheritance
class Person:
    def walk(self):
        print("Person is walking")
    def read(self):
        print("Person is reading")
class Student(Person):
    def exam(self):
        print("Student attending exam")
pe=Person()
pe.walk()
pe.read()

st=Student()
st.exam()
st.walk()
st.read()