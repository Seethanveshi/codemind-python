a,b=map(int,input().split())
for i in range(1,b+1,2):
    if i%2!=0:
        print(a,"x",i,"=",a*i)