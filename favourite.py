x=input("Enter A for favourite books, B for favourite movies and C for fovourite songs: ")
if x=="A":
    A=eval(input("Enter list of favourite books: "))
elif x=="B":
    B=eval(input("Enter list of favourite movies: "))
else:
    C=eval(input("Enter list of favourite songs: "))

with open("favourite.txt","w") as f:
    f.writelines(A)
    f.writelines(B)
    f.writelines(C)
with open("favourite.txt","r") as f:
    book=f.readlines(A)
    songs=f.readlines(C)
    movies=f.readlines(B)
for i in book:
    print(i)
for i in songs:
    print(i)
for i in movies:
    print(i)