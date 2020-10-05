#WAP to accept word and check if it is palindrome
str=input("Enter String-").upper()
newstr= ""
for i in range(len(str),0,-1):
    a=str[i-1]
    newstr = newstr+a
if str == newstr:
    print("Palindrome")
else:
    print("Not Palindrome")
