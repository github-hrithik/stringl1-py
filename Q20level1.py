#WAP to accept a sentence and display the words having length is greater than 5
sen=input("Enter Sentence-").strip()
lst=sen.split()

for i in range(len(lst)):
    if i == len(lst)-1:
        final=lst[i].split(".")
        if len(final[0])>5:
            print(final[0])
    else:
        if len(lst[i])>5:
            print(lst[i])
