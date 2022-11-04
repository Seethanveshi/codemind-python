n=int(input())
l=list(map(int,input().split()))
s=set(l)
l=list(s)
c=0
for i in l:
    if i%2!=0:
        c+=1
print(c)