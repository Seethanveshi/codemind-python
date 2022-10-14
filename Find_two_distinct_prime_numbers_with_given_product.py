n=int(input())
c=0
l=[]
for i in range(1,n,1):
    c=0
    for j in range(1,i+1,1):
        if i%j==0:
            c+=1
    if c==2:
        l.append(i)
for k in l:
    for k1 in l:
        if k*k1==n:
            print(k,k1)
            break
    if k*k1==n:
        break
if k*k1!=n:
    print("-1")