n1=int(input())
n2=int(input())
i=1
c=0
while True:
    t=n1+n2+i
    for j in range(1,t+1,1):
        if t%j==0:
            c+=1
    if c==2:
        print(i)
        break
    else:
        i+=1
        c=0