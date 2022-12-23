f=open("line.txt","r+")
line=f.read(20)
print(line)
print(f.tell())
line=f.readline()
print(line)
f.close
