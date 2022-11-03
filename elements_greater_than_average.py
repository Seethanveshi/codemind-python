n=int(input())
l=list(map(int,input().split()))
s=sum(l)
l1=len(l)
c=0
avg=s//l1
for i in l:
    if i>=avg:
        c+=1
print(c)