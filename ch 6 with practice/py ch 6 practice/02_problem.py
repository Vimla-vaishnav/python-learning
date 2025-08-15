marks1 = int(input("Science:"))
marks2 = int(input("Social study:"))
marks3 = int(input("Mathematics:"))

#number input karne ke liye int ka type jarur likhe
# check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass",total_percentage)

else:
    print("You failed, try again next year!",total_percentage)
# percentage 40 se jyada hone chahiye or marks 33 se jyada ho to pass hoga