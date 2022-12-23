a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a>b>c:
    print("Largest number is: ",a)
elif a<b>c:
  print("Largest number is: ",b)
else:
  print("Largest number is" ,c)
print("Do you want to find the largest number again?")
print("Type 1 if yes else type 2")
if input(1):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    if a>b>c:
      print("Largest number is: ",a)
    elif a<b>c:
      print("Largest number is: ",b)
    else:
      print("Largest number is" ,c)
if input(2):
  print("Thank you for using")
    
