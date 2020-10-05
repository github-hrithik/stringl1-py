#WAP to accept a day name and display the Day number.(eq- Monday --1)
day=input("Enter Day Name-")
name=day.upper()
if name== "MONDAY":
    print("1")
elif name== "TUESDAY":
    print("2")
elif name== "WEDNESDAY":
    print("3")
elif name== "THURSDAY":
    print("4")
elif name== "FRIDAY":
    print("5")
elif name== "SATURDAY":
    print("6")
elif name== "SUNDAY":
    print("7")
else:
    print("Invalid input")
