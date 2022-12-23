stack = []
top = None
def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False
def push(ele):
    stack.append(ele)
    top = len(stack) - 1
def pop():
    if isEmpty():
        print("underflow")
    else:
        item = stack.pop()
        if len(stack) == 0 :
            top = None
        else:
            top = len(stack) - 1
        return(item)
def display():
    if isEmpty():
        print("No elements present")
    else:
        top = len(stack) - 1
        print(stack[top] + " <- Top")
        for a in range(top-1,-1,-1):
            print(stack[a])
def peek():
    if isEmpty():
        print("The stack is empty")
    else:
        top = len(stack) - 1
        return(stack[top])


while True:
    a=int(input("Enter 1)push 2)pop 3)display 4)peek: "))
    if a==1:
        b=input("Enter the element u want to push: ")
        push(b)

    elif a==2:
        c=input("Enter the element u want to pop: ")
        print("element popped: ",Pop(c))

    elif a==3:
        display()
    elif a==4:
        e=input("Enter the element u want to peek: ")
        peek(e)

    else:
        print("Choose a correct option")
        break
            
            
        
        
