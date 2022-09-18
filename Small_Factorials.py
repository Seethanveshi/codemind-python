t=int(input())
for i in range(t):
    n=int(input())
    f=1
    for j in range(n,0,-1):
        f=f*j
    print(f)