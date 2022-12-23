#WAP  using function that accepts a list and finds the sum of all numbers in the list
def s(a):
    a=sum(a)
    return a

a=eval(input("Enter a list: "))
print("The sum of the elements is: ",s(a))
