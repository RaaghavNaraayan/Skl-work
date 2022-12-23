def power(b,p):
    print("This is the power function")
    y=b**p
    return y

def calcsquare(x):
    print("This is the square function")
    a=power(x,2)
    return a

n=5
result=calcsquare(n)+power(3,3)
print(result)
