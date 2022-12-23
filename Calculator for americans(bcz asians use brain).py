def compute():
    print("Enter 'a' for addition, 's' for subtraction, 'd' for division and 'm' for multiplication")
    ch=input(x,y)
    if ch=='a':
        solution=a+b
        history.append(solution)
    elif ch=='s':
        if a>b:
            solution=a-b
        else:
            solution=b-a
        history.append(solution)
    elif ch=='m':
        solution=a*b
        history.append(solution)
    elif ch=='d':
        solution=a/b
        history.append(solution)
    print(solution)
def recall():
    global history
    if len(history)==0:
        print("There is no history.")
    else:
        print("Log-")
        history=history[::-1]
        for i in history:
            print(i)
history=[]
take_input= True
while(take_input):
    print("Press 1 to compute, 2 for history and 3 to quit program")
    choice=int(input())
    if choice==1:
        a=float(input("Enter number 1= "))
        b=float(input("Enter number 2= "))
        compute(a,b)
    elif choice==2:
        recall()
    elif choice==3:
        print("End")
        take_input=False
    else:
        print("Invalid Input")
        



    
    




