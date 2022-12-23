array = []
def insert():
    row = int(input("Enter the no of rows"))
    col = int(input("Enter the no of columns"))
    for r in range(row):
        rows = []
        for c in range(col):
            ele = input("Enter the element to be added:")
            rows.append(ele)
        print("Next row")
        array.append(rows)
def display():
    row = len(array)
    for r in range(row):
        print("|",end='')
        col = len(array[r])
        for c in range(col):
            print(array[r][c],end='|')
        print()
def delete():
    e = int(input("Enter the row index:"))  
    f = int(input("Enter the column index:"))
    print("Element deleted is ",array[e].pop(f))
            
while True:
    i = int(input("Enter a choice(1)insert(2)display(3)delete(4)quit"))
    if i == 1:
        insert()
    elif i == 2:
        display()
    elif i == 3:
        delete()
    elif i == 4:
        print("Quitting program")
        break
    else:
        print("Invalid Choice")
