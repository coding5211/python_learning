# coing=UTF-8
class SchoolMember:
    """代表学校里的成员"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("(Initialized SchoolMember {})".format(self.name))

    def tell(self):
        print("Name = {}, Age = {}".format(self.name,self.age),end=" ")

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print("Initialized Teacher {}".format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print("Salary = {}".format(self.salary))

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print("Initialized Student {}".format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print("Marks = {:d}".format(self.marks))


t = Teacher("jack",40,5000)
s = Student("rose",18,130533)

print()

members = [t,s]
for member in members:
    member.tell()
