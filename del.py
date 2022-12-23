#WAP to creat a binary file with the following data as seperate python
#objects:name,age,class.Delete all student data belonging to class 9.
#While reading filter the data but append everything.
import pickle as p
l=[]
with open('Student data.dat','wb') as f:
    n=int(input("Enter no. of students:"))
    for i in range(n):
        name=input("Enter full name of the student:")
        age=int(input("Enter the age of student:"))
        grade=int(input("Enter grade of student:"))
        l.append(name)
        l.append(age)
        l.append(grade)
        p.dump(l,f)
    print(l)

with open('Student data.dat','rb') as f:
    L=p.load(f)
    for i in range (len(L)):
        if L!=9:
            print(L)
    
        
    

