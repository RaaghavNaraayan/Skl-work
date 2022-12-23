#display the size of a file after removing blank chars,whitespaces, newlines etc
g=0
with open("sample.txt","r") as f:
    s=f.read()
    for i in s:
        if not i==' ':
            g+=1
print("The number of chracters are: ",g)
        
    
