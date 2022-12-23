#write a program to find factorial of a number using user defined funcion
def fact(n):
    f=1
    for i in range (1,n+1):
     f*=i
     return fact
     

n=int(input("Enter the number: "))
print(fact(n))