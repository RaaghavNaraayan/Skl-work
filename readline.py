with open("journal.txt","w") as f:
    L=("Variable names cannot start with a number")
    f.write(L)

with open("journal.txt","r") as f:
    str=f.readline()
for ch in str:
    if ch==' ':
       print('#',end='')
    else:
       print(ch,end='')
    
