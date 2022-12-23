with open("Favbooks.txt","r") as f:
    a=f.read()
    print(a.replace("c","C"))
with open("Favbooks.txt","w") as f:
    f.write(a.replace("c","C"))
