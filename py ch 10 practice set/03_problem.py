class Demo:
    a = 4

object = Demo()
print(object.a) # Prints the class attribute because instance attribute is not present
object.a = 0  # Instance attribute is set
print(object.a)# Prints the class attribute because instance attribute is present
print(Demo.a) # Prints the class attribute
#class attribute change nahi hua