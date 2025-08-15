class Employee:
    a = 1 # class value
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45 # Instance value
e.show()
# class method me class value ko hi dikha