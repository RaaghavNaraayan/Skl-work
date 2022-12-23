with open ("Favbooks.txt","w") as f:
    l=["Holes\n","The martian\n","Russian roulette\n","The last mission\n"]
    f.writelines(l)
with open("Favbooks.txt","r") as f:
    lr=f.readline()
    print(lr)

for item in lr:
    print(item)
#just like write lines(),we have a readlines() function that reads the text in the file as a list of items,
#  where each item represents a line of data in a file. (You need to add a newliner character at the 
# end of each item while writing in order to print the output on different lines.) 
# To print the information stored in readlines(),we use a for loop and print each item in the list.