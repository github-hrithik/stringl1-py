#WAP to accept two strings and tell which comes later in lexicographics order(dictionary order). If
#equal how appropriate message.
str1=input("Enter String 1-")
str2=input("Enter String 2-")
if str1>str2:
    print("1.",str2,"\n2.",str1)
elif str2>str1:
    print("1.",str1,"\n2.",str2)
else:
    print("Both sre same!")
