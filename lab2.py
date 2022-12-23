import random
def ran(a):
    x=10**(a-1)
    y=(10**a)-1
    z=random.randint(x,y)
    return z

a=int(input("Enter a number: "))
print("The randomly generated number is: ",ran(a))
