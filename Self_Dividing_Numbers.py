n1=int(input())
n2=int(input())
for i in range(n1,n2+1,1):
    l=[]
    x=i
    while i>0:
        r=i%10
        l.append(r)
        i=i//10
    l2=[]
    for j in l:
        if j==0:
            break
        elif x%j==0:
            l2.append(j)
    if len(l)==len(l2):
        print(x,end=" ")