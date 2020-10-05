#WAP to accept a String and Convert the case of each alphabet present in it.
str=input("Enter String-")
newstr= ""
for i in str:
    if i.isupper()==True:
        newstr=newstr+i.lower()
    else:
        newstr=newstr+i.upper()
print(newstr)
