class Employee:
    '所有员工的基类'
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print("Total Employee %d" %Employee.empCount)
    def displayEmploye(self):
        print("Name:",self.name,"Salary:",self.salary)
'''
emp1=Employee("Zara",2000)
emp2=Employee("Manni",5000)
emp1.displayEmploye()
emp2.displayEmploye()
emp1.age=7
emp1.age=8
del emp1.age
setattr(emp1,"age",9)
delattr(emp1,"age")
setattr(emp1,"age",8)
hasattr(emp1,"age")
getattr(emp1,"age")
print("Total Employee:%d" % Employee.empCount)
'''
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__dict__)