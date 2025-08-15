'''
factoraial(0) = 1
factoraial(1) = 1
factoraial(2) = 1 X 2
factoraial(3) = 1 X 2 X 3
factoraial(4) = 1 X 2 X 3 X 4
factoraial(5) = 1 X 2 X 3 X 4 X 5

factorial(n) = n X n -1 X........3 X 2 X 1

factorial(n) = n * factorial (n-1)
'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is:{factorial(n)}")