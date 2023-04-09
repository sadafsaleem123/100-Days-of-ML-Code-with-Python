class Employee:
    def __init__ (self, first, last):
        self.first = first
        self.last = last

#object of class Employee
emp_1 = Employee('Nobita', 'Ahmed')
emp_2 = Employee('Shezooka', 'Ahmed') 

#print(emp_1)
#print(emp_2)

#instance of class Employee
print(emp_1.first)
print(emp_2.first)

