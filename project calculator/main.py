def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operation(+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error:do not divided by zero!")
            return
        
    else:
        print("Error:invalid operation!")
        return
    print("Result:",result)
calculator()