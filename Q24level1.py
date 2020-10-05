#WAP to assign 7 country names and corresponding wonder names in two separate arrays and
#after that search a given country name and display related wonder name.
wonders=["THE GREAT WALL OF CHINA",
         "CHRIST THE REDEEMER",
         "MACCHU PICCHU",
         "CHIZEN ITZA",
         "THE COLLOSEUM",
         "TAJ MAHAL",
         "PETRA"]
countries=["CHINA","BRAZIL","PERU","MEXICO","ITALY","INDIA","JORDAN"]
query=input("Enter Name of the Country-").upper()
ctr=0
if query in countries:
    print(query,"has",wonders[countries.index(query)])
else:
    print("The given Country does not have a wonder or the name is misplelled!")
