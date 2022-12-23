#wap to accept name,age and salary from the users in a menu driven format until the user decides to quit the program and
#write each user data as a list into a binary file. Read and display the data from the binary file where the last name is kumar
import pickle
number_of_data=int(input("Enter the number of users you want to enter: "))
data=[]
for i in range(number_of_data):
    raw=input("Enter name"+str()+":")
    age=input("Enter age"+str()+":")
    salary=input("Enter salary"+str()+":")
    data.append(raw)
    data.append(age)
    data.append(clas)
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


