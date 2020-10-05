#WAP to accept name, marks of five students and create merit list based on marks
dic=dict()
for i in range(5):
    name=input("Enter name of student"+str(i+1)+"-")
    marks=int(input("Enter marks of student"+str(i+1)+"-"))
    dic[marks]=dic.get(marks,name)
lst=sorted(dic.keys(),reverse=True)
print("\nMERIT LIST-")
for i in lst:
    print(dic[i])
