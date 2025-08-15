a = 89 # global value
def fun():
    global a # jab global likhenge tab global value change hoti hai
    a = 3

    print(a)
fun()
print (a)