def myfunc(mylist):
    print("list recieved",mylist)
    new=[3,5]
    mylist=new
    mylist.append(6)
    print("List after change: ",mylist)
    return

list1=[1,4]
print("List before func call",list1)
myfunc(list1)
print("List in main after function call",list1)
global list1[4,5]
