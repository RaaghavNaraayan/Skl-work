#Write a function that takes two numbers and returns the number has minimum one's digit.
def mini(r,s):
    if str(r)[len(str(r))-1]<str(s)[len(str(s))-1]:
     return(r)
    return(s)
    
r=int(input("Enter a number: "))
s=int(input("Enter a number: "))
print(mini(r,s))
       
    
