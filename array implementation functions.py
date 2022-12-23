array=[]
def insert(ele):
    pos=int(input("Enter the position you want to insert in: "))
    array.insert((pos-1),ele)

    
def delete():
    pos=int(input("Enter the position you want to delete in: "))
    if len(array)>=pos:
        array.pop((pos-1))
    else:
        print("Len of the array is less than the position given")

def display():                        #This makes sure we only print the elements in the list and not the entire list
    for i in array:
        print(i)

while True:
    a=int(input("Enter 1 to insert an element, Enter 2 to delete an element, Enter 3 to display the elements in the list and any other number to quit the program: "))
    if a==1:
        b=input("Enter the elemnt you want to insert: ")
        insert(b)
    elif a==2:
        delete()
    elif a==3:
        display()
    else:
        print("Quitting program 101")
        break
      
