x,y=map(int,input().split())
z=x+(y*2)
if x==0 and y%2==1:
    print("NO")
elif z%2==0:
    print("YES")
else:
    print("NO")