class Employee:
    name = "Harry"
    language = "py"
    salary = 1200000

harry = Employee()
print(harry.name,harry.language)

# name hate ke or 
class Employee:
    language = "py" # This is a class attribute
    salary = 1200000

harry = Employee()
print(harry.salary,harry.language)
 
rohan = Employee()
print(rohan.salary,rohan.language)

# aise bhi name add kar sakte hai
class Employee:
    language = "py"
    salary = 1200000

harry = Employee()
harry.name ="Harry Das" # This is instance attribute
print(harry.name,harry.salary,harry.language)
 
rohan = Employee()
rohan.name = "Rohan sharma"
print(rohan.name,rohan.salary,rohan.language)

# Here name is object attribute and salary and language are class attribute as they directly belong to the class