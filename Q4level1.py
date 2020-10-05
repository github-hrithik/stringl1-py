#Count Number of vowels

st=input("Enter String-")
stf=st.upper()
ctr=0
for i in stf:
    if i in ["A","E","I","O","U"]:
            ctr+=1
print(ctr)
