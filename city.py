#insert(city) and delete(city) methods in python to add city and remove city considering them to act as push and pop operations of the data structure stack
stack = []
top = None
def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False
def insert(city):
    stack.append(city)
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

while True:
    a=int(input("Enter 1 to push and 2 to pop: "))
    if a==1:
        b=input("Enter the city name you want to enter: ")
        insert(b)
    elif a==2:
        print(pop())
    else:
        break
