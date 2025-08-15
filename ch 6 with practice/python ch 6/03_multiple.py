a = int(input("Enter your age:"))
# multiple if statement
#if statement no 1
if(a%2 == 0):
    print("a is even")
# End of statement no 1

# if statment no 2
if(a>=18):
    print("your are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("you are entering 0 which is not a valid age")

else:
    print("your are below the age of consent")

# End of statement no 2

print("End of programme")

# if single ho sakta hai par else or elif single nhi ho sakta