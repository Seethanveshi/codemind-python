n=int(input())
n1=0
a,b=0,1
c=0
if n==1:
    print(a)
else:
    while c<n:
        print(a,end=" ")
        n1=a+b
        a=b
        b=n1
        c+=1
