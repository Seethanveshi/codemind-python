n=int(input())
l=list(map(int,input().split()))
l1=len(l)
if l1%2==0:
    print(*l)
else:
    l.append(0)
    print(*l)