# 5! =1 X 2 X 3 X 4 X 5 factorial
n = int(input("Enter the number: "))
product = 1
for i in range(1,n+1):
    product = product * i

print(f"The factorial of {n} is {product}")
# n+1 likhana hai tab pura number lehega
#jaise 1 se 5 likho tab 4 tak hi count hoga is liye n +1 lana hoga