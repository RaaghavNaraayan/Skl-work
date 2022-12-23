with open("A.txt","w") as f:
    f.write("12B")
    f.write("Computer science")


with open("A.txt","r") as f:
    print(f.read())

with open("A.txt","a") as f:
    f.write("user defined function")

with open("A.txt","r") as f:
    print(f.read())
    
