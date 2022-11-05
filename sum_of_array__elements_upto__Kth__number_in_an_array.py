n=int(input())
l=list(map(int,input().split()))
a=int(input())
s=0
for i in l:
    s+=i
    if i==a:
        break
print(s)