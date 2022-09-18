n1=int(input())
n2=int(input())
c=0
for i in range(n1,n2+1,1):
    for j in range(1,i+1,1):
        if i%j==0:
            c+=1
    if c==2:
        print(i)
        c=0
    else:
        c=0