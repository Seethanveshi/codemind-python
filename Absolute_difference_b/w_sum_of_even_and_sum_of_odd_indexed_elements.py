n=int(input())
l=list(map(int,input().split()))
e,o=0,0
for i in range(len(l)):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
if e>=o:
    print(e-o)
else:
    print(o-e)