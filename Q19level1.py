#WAP to accept a String and Display it in Title Case.(eq- My name is covid----- My Name Is Covid)
sen=input("Enter the sentence-").strip()
lst=sen.split()
newsen = ""
for i in range(len(lst)):
    if i==len(lst)-1:
        newsen=newsen+lst[i].capitalize()+"."
    else:
        newsen=newsen+lst[i].capitalize()+" "
print(newsen)
