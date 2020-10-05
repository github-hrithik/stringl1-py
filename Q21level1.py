#WAP to accept a sentence and extract the palindrome words.

lst=input("Enter Sentence-").strip().split()
lst1=[]
for i in range(len(lst)):
    str1=lst[i].split(".")
    str=str1[0]
    newstr= ""
    for j in range(len(str),0,-1):
        newstr=newstr+str[j-1]
    if newstr == str:
        lst1.append(str)

print(lst1)
