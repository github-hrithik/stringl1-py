#WAP to accept a word and convert it to piglatin form(trouble --- oubletray)
str=input("Enter String-")
newstr= ""
initial= ""
lst=["a","e","i","o","u"]
for i in range(len(str)):
    if str[i].lower() in lst:
        newstr=str[i:]
        break;
    else:
        initial=initial+str[i]
print("Piglatin Form-",newstr+initial+"ay")
