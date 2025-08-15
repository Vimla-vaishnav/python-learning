class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}.")

class coder:
    language = "Python"
    def printLanguage(self):
        print(f"out of all the language here is your language: {self.language}.")



class Programmer(Employee,coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The comapany is {self.company} and he is good with{self.language} language.")




a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()
