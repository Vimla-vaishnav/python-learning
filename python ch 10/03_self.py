class Employee:
    language = "py" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    def greet(self):
        print("Good morning")

harry = Employee()
harry.language ="JavaScript" # This is instance attribute
harry.getInfo()
harry.greet()
# Employee.getInfo(harry)

# static method
class Employee:
    language = "py" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod # statics mode se self nhi likhana hoga
    def greet():
        print("Good morning")

harry = Employee()
harry.language ="JavaScript" # This is instance attribute
harry.getInfo()
harry.greet()


