def product(a,b):
    #product of 2 numbers
    print(a*b)

def subtract(a,b):
    #subtract 2 numbers
    print(a-b)

def add(a,b):
    #add 2 numbers
    print(a+b)
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("1=add, 2=subtract and 3=multiply: "))
if c==1:
    add(a,b)
      
elif c==2:
    subtract(a,b)
    
    
else:
    product(a,b)

