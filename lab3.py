def com(p,r,n,t):
    x=p*((1+(r/100)/n))**(n*t)-p
    return x

p=int(input("Enter the principal amount: "))
r=int(input("Enter the rate: "))
n=int(input("Enter the interest for the given amount: "))
t=int(input("Enter the time in months: "))
print("The compound interest will be: ",com(p,r,n,t))
