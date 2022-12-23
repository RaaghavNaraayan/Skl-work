#WAP to search a record from the binary file
import pickle
number_of_data=int(input("Enter the number of users you want to enter: "))
data=[]
for i in range(number_of_data):
    raw=input("Enter name"+str()+":")
    age=input("Enter age"+str()+":")
    clas=input("Enter class"+str()+":")
    data.append([raw,age,clas])
file=open("important.dat","wb")
pickle.dump(data,file)
file.close

file=open("important.dat","rb")
data=pickle.load(file)
print(data)
m=input("Enter the name you want to search: ")
for i in data:
    if i[0]==m:
        print("The name is: ",i[0])
        print("The age is: ",i[1])
        print("The class is: ",i[2])
        break
    else:
        print(data)
 
