#write a menu driven program which performs all the basic operations using dictionary on student binary file such as inserting,reading,updating,searching and deleting a record
import pickle
while True:
    a=int(input("Enter 0 to start/continue the program, 1 to display the contents and 2 to exit the program: "))
    if a==0:
        number_of_data=int(input("Enter the number of users you want to enter: "))
        beta={}
        for i in range(number_of_data):
            raw=input("Enter name"+str()+":")
            age=input("Enter age"+str()+":")
            clas=input("Enter class"+str()+":")
            combi=input("Enter the combination"+str()+":")
            beta.update({raw:[age,clas,combi]})
    elif a==1:
        print(beta)
    else:
        break
            
file=open("important.dat","wb")
pickle.dump(beta,file)
file.close

file=open("important.dat","rb")
data=pickle.load(file)
print(beta)

