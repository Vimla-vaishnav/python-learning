class Employee:
    a = 1 # class value
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    
    @property 
    def name(self):
        return f"{self.fname} {self.lname}"     
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    



e = Employee()
e.a = 45 # Instance value
e.name = "Harry Khan"
print(e.name)
e.show()
# class method me class value ko hi dikha
# encapsulation means that you can't see te implementation details are encapsulated
# abstraction means that we have hidden the implemention details