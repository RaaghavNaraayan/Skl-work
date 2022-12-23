#WAP that generates a series using a function which takes first and last values of the series and then generates 4 terms that are equidistant from each other
def series(a,b):
    c=2
    l=[]
    for i in range(a,b+1):
        if c%2==0:
            print(i,end=",")
            
        
