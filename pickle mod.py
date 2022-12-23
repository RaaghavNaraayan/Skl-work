import pickle
number_of_data=int(input("Enter the number of data: "))
data=[]
for i in range(number_of_data):
    raw=input("Enter data"+str(i)+":")
    data.append(raw)
file=open("important.dat","wb")
pickle.dump(data,file)
file.close

file=open("important.dat","rb")
data=pickle.load(file)
print(data)
while True:
    try:
        print(pickle.load(file))

    except EOFError:
        break
file.close
   


