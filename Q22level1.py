#WAP to accept a sentence and display the words having double sequences.(eq- I Like Rabbit----rabbit)
lst=input("Enter Sentence-").strip().split()
last= ""
lst1=[]
for i in lst:
    for char in i:
       if char == last:
           lst1.append(i)
           last=char
           continue
       else:
           last=char
print(lst1)
