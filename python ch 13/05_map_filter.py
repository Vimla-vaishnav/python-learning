from functools import reduce
# map example

l = [1, 2, 3, 4, 5, 6]
square = lambda x: x*x

sqlist = map(square, l)
print(list(sqlist))


# Filter example

def even(n):
    if (n%2 == 0):
        return True
    return False
onlyEven = filter(even,l) 
print(list(onlyEven))

# Reduce Example
def  sum (a ,b):
    return a + b
print(reduce(sum, l))
# is reduce me pahle do number ka add hoga phir isko answer age badega