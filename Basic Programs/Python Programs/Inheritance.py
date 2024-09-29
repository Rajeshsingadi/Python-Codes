#Inheritance

class Person( object ):
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def display(self):
        print(self.name)
        print(self.address)

    def employeeDetails(self):
        print(self.address)

class Employee(Person):
    def __init__(self, name, address, empId, empSalary):
        self.empId = empId
        self.empSalary = empSalary
    
        Person.__init__ (self, name, address)#invoking the __init__ of the parent class

    def employeeDetails(self):
        print("My name is {}".format(self.name))
        print("My address is {}".format(self.address))
        print("The empId is : ", self.empId)
        print("The empId is : ", self.empSalary)

a = Employee("fruity", "bangalore", 560305, 1200000 )
a.display()
a.employeeDetails()