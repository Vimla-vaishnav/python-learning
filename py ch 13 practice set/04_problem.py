def divisibile5(n):
    if (n%5 == 0):
        return True
    return False

a = [ 1,2,57,65,76,55,767, 45]

f = list (filter(divisibile5, a))
print(f)