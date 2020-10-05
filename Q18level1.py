#WAP to accept a String count the frequency of each alphabet in the String.
str=input("Enter String-").strip()
dic= dict()
for i in str:
    dic[i]=dic.get(i,0)+1
for k,v in dic.items():
    print(k,"->",v)
