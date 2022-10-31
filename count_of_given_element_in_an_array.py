n=int(input())
l=list(map(int,input().split()))
e=int(input())
c=0
for i in l:
    if i==e:
        c+=1
print(c)