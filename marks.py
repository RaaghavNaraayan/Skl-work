import csv
fields=["Nmae","Class","Year","Percent"]
rows=[["Rohit","12","2003","92"],
      ["Shama","12","20003","34"],
      ["Pene","23","3445","34"]]

with open("Marks.csv","w",newline="") as f:
    csv=csv.writer(f)
    csv.writerow(fields)
    '''for i in rows:
        csv.writerow(i)'''
    csv.writerows(rows)
    print("File created")
