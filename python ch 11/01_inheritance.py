class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with{self.language} language")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with{self.language} language")

# class employee ko base ya parents class hai.or isme update karoge to puri file update hogi
# class programmer inheritance class hai ya child



a = Employee()
b = Programmer()

print(a.company,b.company)
