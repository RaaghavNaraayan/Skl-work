import csv
a=0
with open("Marks.csv","r")as f:
    csv=csv.reader(f)
    '''for row in csv:
       print(row)'''
    '''col=next(csv)
    print(col)'''
    for i in csv:
        a+=1
    print("No of row:",a)
    

