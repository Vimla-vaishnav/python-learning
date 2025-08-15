friends = ["Apple","Orange",5,345.06,False,"Aakash","Rohan"]

print (friends)
#append last list add kar sakte hai
#list ko change kr sakte hai
friends .append("Drisha") #append method
print (friends)

#sort method
li = [1,34,62,2,6,11]
li.sort()
print(li)

#reverse method
li = [1,34,62,2,6,11]
li.reverse()
print(li)

#insert method
li = [1,34,62,2,6,11]
li.insert(3,468) #insert 468 such that its index in the list is 3
print(li)

#pop method
li = [1,34,62,2,6,11]
li.pop(3)
print(li)

#li.pop ko print karoge to value dikhega or second option value wala example
li = [1,34,62,2,6,11]
value = li.pop(3)
print(value)

#remove method
li = [1,34,62,2,6,11]
li.remove(62)
print (li) 