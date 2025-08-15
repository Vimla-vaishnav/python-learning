name = "harry" #double,single or multi line ke liye triple comma me likha content ko string bolte hai
# ek bar string ban gayi use change nhi kar sakte unmute khate hai
# age letter ki numbering 0 se start hogi or last letter ki -1 se start hogi {show notes}

nameshort = name [0:3] # start from index 0 all the way till 3 {excluding 3}
print(nameshort)
character1 = name [1]
print (character1)

#negative number represent
print (name[-4:-1])
print (name[1:4])

# other advance techniques
print(name[:4]) #is same as print(name[0:4])
print(name[1:]) #is same as print(name[1:5])

# slicing with skip value start here
name = "amazing"
print (name[1:6:2]) 