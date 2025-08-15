'''
For n =3
  *
 ***
*****
For n = 5
    *
   ***
  *****
 *******
*********  
'''
n = int(input("Enter the number: "))
for i in range (1,n+1):
    print(" "*(n-i),end ="")
    print("*"*(2*i-1),end ="") #end new line nahi deta
    print("") #proper way me lane ke liye