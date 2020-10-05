#WAP to accept String and Convert its individual characters to capital and Small alternately.(Amar----- aMaR)
str=input("Enter String-").strip()
newstr= ""
for i in range(len(str)):
    if i%2==0:
        newstr=newstr+str[i].upper()
    else:
        newstr=newstr+str[i].lower()
print(newstr)
