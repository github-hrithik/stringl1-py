#Print Capital Letters
x=input("Enter String-")
ctr=0
for i in x:
    if i>="A" and i<="Z":
        print(i)
        ctr+=1
print("The total number of capital letter-",ctr)
