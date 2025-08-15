class Employee:
    language = "py" # This is a class attribute
    salary = 1200000

    def __init__(self,name,salary,language):  # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")

drisha = Employee("Drisha",1300000,"JavaScript")
drisha.name ="Drisha" # This is instance attribute

print (drisha.name,drisha.salary,drisha.language)
 
# harry = Employee()

