#WAP to accept roll no, name of 5 students and display them back on the screen in tabular form.
names = []
marks = []
for i in range(5):
    name=input("Enter name of student "+str(i+1)+"-")
    names.append(name)
    mark=input("Enter marks of student "+str(i+1)+"-")
    marks.append(mark)
print("\tNAME\t\tMarks")
for i in range(5):
    print("\t"+names[i]+"\t\t"+marks[i])
