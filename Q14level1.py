#WAP to replace “15 august” with “26 january” and “independence” with “republic” in the string
#“15 august is independence day”
str="15 august is Independence day"
lst=str.split()
lst[0]="26"
lst[1]="January"
lst[3]="Republic"
str2= ""
for i in lst:
    str2=str2+" "+i
print(str,"->",str2.lstrip())    
