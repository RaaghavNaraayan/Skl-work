#WAP to create an excel sheet which stores employee's details like name,age and salary. Take a user input for the name and search for the employee details in the same file.
import csv
fields=["Name","Age","Salary"]
l=[]
n=int(input("Enter the number of employee's details u want to file: "))
for i in range(n):
    name=str(input("Enter the employee's name: "))
    age=int(input("Enter the age of the employe: "))
    sal=int(input("Enter the salary of the employe: "))
    l.append([name,age,sal])
    print(l)

with open("emplo.csv","w",newline="") as f:
    cs=csv.writer(f)
    cs.writerow(fields)
    cs.writerows(l)
    print("file created")

y=0
while y==0:
    na=str(input("Enter the name of the employee you want the details of: "))
    with open("emplo.csv","r") as f:
        csv=csv.reader(f)
        for i in csv:
            if i[0]==na:
                print(i)

        else:
            print("Program ended")
            break
    
    
    
    
    
