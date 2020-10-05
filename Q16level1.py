#WAP in java to accept 5 String/Name and Display the names that start with a Vowel
lst= list()
lst1= list()
for i in range(5):
    x=input("Enter String-").strip().upper()
    lst.append(x)
    if lst[i][0] in ["A","E","I","O","U"]:
        lst1.append(x)

print(lst1)
