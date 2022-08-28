t=int(input())
c=0
for i in range(1,t+1,1):
    l,r=map(int,input().split())
    for j in range(l,r+1,1):
        if j%10==2 or j%10==2 or j%10==3 or j%10==9 or j==2 or j==3 or j==9:
            c+=1
    print(c)
    c=0