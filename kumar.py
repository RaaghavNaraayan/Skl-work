'''Write a program to accept name,age and salary from the users
(in a menu driven format until the user decides to quit programn).
And write each user data as a list into a binary file.
Read and display the data from the binary file where the last name
is Kumar'''

l=[]
import pickle
name1=''
name2=''
age=[]
salary=[]
def select():
    print("1.Enter data 2.Display data 3.Quit")
    n=int(input("Enter a number based on your selection:"))
    if(n==1):
        enter()
    if(n==2):
        display()
    if(n==3):
        print("Exiting program")
        

def enter():
    global name1
    global name2
    global age
    global salary
    name1=input("Enter your first name:")
    name2=input("Enter your second name:") 
    age=int(input("Enter you age:"))
    salary=int(input("Enter your salary:"))
    l.append(name1)
    l.append(name2)
    l.append(age)
    l.append(salary)
    with open ('Info.dat','wb') as f:
        pickle.dump(l,f)
    select()

def display():
    global name1
    global name2
    global age
    global salary
    with open ('Info.dat','rb') as f:
        l=pickle.load(f)
        print(l)
        for i in range(len(l)):
            if l[i]=="Kumar" or l[i]=="kumar":
                print("name:",name1,name2,"age:",age,"salary:",salary)
        while True:
            try:
                print(pickle.load(f))

            except EOFError:

                break

    select()

select()


