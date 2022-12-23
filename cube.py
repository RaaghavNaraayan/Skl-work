#WAP to find the cube of a number x which is taken input outside the function and returned to the main program after the calculations
def cube(x):
    x=x*x*x
    return x
x=int(input("Enter the number: "))
print(cube(x))
