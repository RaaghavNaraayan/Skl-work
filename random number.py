#WAP that recieve 2 numbers and generates a random number from the range, using this range generate 3 random numbers within the range
def randm(r,s):
    import random
    return random.randint(r,s)


import random
r=int(input("Enter a number: "))
s=int(input("Enter a number: "))
c = r -1
for i in range(3):
    t = randm(r,s)
    print(t-c)
    c -= 1
    
    
