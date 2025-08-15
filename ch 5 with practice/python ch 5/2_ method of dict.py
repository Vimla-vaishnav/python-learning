marks ={
    "Harry" : 100,
    "shubham" : 56,
    "rohan" : 23,
     0 : "bitu"
}
print(marks.items()) #list banati hai
print(marks.keys())#keys dikhati[jaise ki harry,shubham etc]
print(marks.values())#values dikhati [marks]
#update me name add kar sakte hai or jo ho usme edit kar sakte hai
marks.update({"Harry":99,"rina":86})
print(marks)
print(marks.get("Harry2")) # prints none
print(marks["Harry2"]) # return an error