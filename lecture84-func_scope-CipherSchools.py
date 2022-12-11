# scope
x = 5 # gloabal variable
def func():
    global x
    x = 7 # local variable
    return x

print(x)
print(func())
print(x)