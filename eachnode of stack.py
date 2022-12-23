#Each node of a stack contains the following information:
#i)pin code of a city
#ii)name of the city
#Write a program to implement the following operations in the above stack
#a)Push the node in to the stack
#b)POP to remove the node from the stack

Stack=[]
Top=None
def push(e):
    Stack.append(e)
    Top=len(Stack)-1

def isEmpty():
    if len(Stack)==0:
        return True
    else:
        return False


def  Pop(Stack):
    if isEmpty(Stack):
        print("Underfow")
    else:
        item=Stack.pop()
        if len(Stack)==0:
            Top=None
        else:
            Top=len(Stack)-1
    return item

def display():
    if isEmpty(Stack):
        print("Underflow")
    else:
        for a in range(Top-1,-1,-1):
            print(Stack[a])

def Peek():
    if isEmpty(Stack):
        return("Underflow")
    else:
        Top=len(Stack)-1
        return(Stack[Top])

while True:
    l=[]
    a=int(input("Enter the pin code of the city: "))
    b=input("Enter the city name: ")
    l.append(a)
    l.append(b)
    print(l)

