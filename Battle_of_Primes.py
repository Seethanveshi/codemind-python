n1=int(input())
n2=int(input())
c=0
i=1
t=n1+n2
while True:
    for j in range(1,t+i+1,1):
        if (t+i)%j==0:
            c+=1
    if c<=2:
        print(i)
        break
    else:
        c=0
        i+=1