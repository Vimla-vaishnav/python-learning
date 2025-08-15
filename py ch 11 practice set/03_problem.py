class Employee:
    salary = 234
    Increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.Increment = ((salary/self.salary) -1 )*100

e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.Increment)