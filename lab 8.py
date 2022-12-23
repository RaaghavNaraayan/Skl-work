with open("file1.txt","r+") as f:
    print(f.read())
    f.seek(0)
    h=input("Enter the colour you want to replace: ")
    for i in h:
        h.replace(i,"white")
        print(f.read())
    
