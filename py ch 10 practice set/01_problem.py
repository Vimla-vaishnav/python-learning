class Programmer:
     company = "Microsoft"
     def __init__(self,name,salary,pin): # double underscore aata hai aage or piche
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry",1200000,245001)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Rohan",1200000,245021)
print(r.name,r.salary,r.pin,r.company)