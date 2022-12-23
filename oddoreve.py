#write a parogram with the function check odd that takes one argument and report if the arguemnt is odd or even
def checkodd(n):
    if n%2==0:
        print("This is an even number")
    else:
        print("This is an odd number")

n=int(input("Enter a number: "))
checkodd(n)
    
