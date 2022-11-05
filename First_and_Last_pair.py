n=int(input())
l=list(map(int,input().split()))
l1=[]
if len(l)%2!=0:
    l.insert(len(l)//2+1,0)
for i in range(len(l)//2):
    l1.append(l[i])
    l1.append(l[len(l)-(i+1)])
print(*l1)