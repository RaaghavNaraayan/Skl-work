#WAP that depending upon user's choice either pushes or pops an element in the stack the elements are shifted towards right so that Top always remains at 0 index
stack = []
top = None
def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False
def push(ele):
    stack.insert(0,ele)
    top = len(stack)-1
def pop():
    if isEmpty():
        print("underflow")
    else:
        item = stack.pop(0)
        if len(stack) == 0 :
            top = None
        else:
            top = len(stack) - 1
        return(item)
def peek():
    if isEmpty():
        print("The stack is empty")
    else:
        top = 0
        return(stack[top])

a=str(input("Enter the stuff u want to enter: "))
push(a)
print(stack)


