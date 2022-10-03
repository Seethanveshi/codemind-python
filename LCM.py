a,b=map(int,input().split())
i=1
while True:
    if i%a==0 and i%b==0:
        print(i)
        break
    else:
        i+=1