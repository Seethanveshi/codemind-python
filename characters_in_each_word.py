s=input()
c=0
c1=0
for i in s:
    if i==" ":
        print(c,end=" ")
        c=0
        c1+=1
    else:
        c+=1
print(c)
