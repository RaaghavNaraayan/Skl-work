with open("sample.txt","w") as f:
    L=["Variable names cannot start with a number\n",
       "Variable names cannot be python keywords\n",
       "Variable names cannot contain whitespaces or special characters other than underscore\n",
       "Variable names can be the length but need to be relevant\n"]
    f.writelines(L)

'''import os
f=open("sample.txt","w")
L=["Hello magane\n","I am your baap\n"]
f.writelines(L)
print(os.getcwd())

f.close()'''

with open ("sample.txt","r") as f:
    str=f.read(41)
    print(str)




















































































  
