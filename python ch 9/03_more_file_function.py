f = open("file.txt")
#1 this is readlines example
# lines = f.readlines()

# print(lines,type(lines))
#f.close()

# 2 here readline

# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))

# line4 = f.readline()
# print(line4,type(line4))

# f.close()

#upar wala chalana ho ctrl + / dabana
# 3 while loops se
line = f.readline()
while(line != ""): #!= is not equal to
    print(line)
    line = f.readline()

f.close( )