#write a program using user defined function to find a prime number
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("This is not a prime number")
            

    print("This is a prime number")

a=int(input("Enter a number: "))
prime(a)
                                                                                                                                                                     
        
