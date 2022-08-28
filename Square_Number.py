n=int(input())
c=0
for i in range(0,n+1,1):
    for j in range(0,n+1,1):
        if (i**2)+(j**2)==n and i!=j:
            c+=1
if c>=1:
    print("True")
else:
    print("False")