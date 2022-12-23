#A line of text is read from the input terminal into stack WAP to output the string in reverse order each character appearing twice

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


def  Pop():
    if isEmpty():
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

a=str(input("Enter a string or line u want to put in the stack: "))
for i in a:
    push(i)
for i in range(len(a)):
    print(Pop()*2,end="")

