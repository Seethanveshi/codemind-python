n1=int(input())
n2=int(input())
for i in range(n1,n2+1,1):
    p=i
    rev=0
    while i>0:
        r=i%10
        rev=rev*10+r
        i=i//10
        if rev==p:
            print(rev,end=" ")