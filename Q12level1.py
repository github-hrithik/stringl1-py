#WAP to accept the name of a person and guess the gender
name=input("Enter Name-").strip().upper()
lst=name.split()
if lst[0] == "MR" or lst[0] == "MASTER":
    print("Male")
elif lst[0] == "MISS" or lst[0] == "KUMARI":
    print("female")
elif lst[0] == "MRS":
    print("female")
else:
    print("Cannot Determine gender")
