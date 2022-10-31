n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
    if i%2!=0:
        s+=l[i]
print(s)