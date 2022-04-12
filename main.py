"""
Create a class Employee with the fields name, salary and designation. Create an object of the class Employee and print it.
"""

class Employee:
  def __init__(self,name,salary,designation):
    self.name = name
    self.salary = salary
    self.designation = designation

  def __str__(self):
    return "Employee Detail: Name: {} and Salary: {} and Designation: {}".format(self.name,self.salary,self.designation)

emp_1 = Employee("Amit", 150000, "Software Developer")
print(emp_1)