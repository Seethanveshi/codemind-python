n=int(input())
f=n
t=n
while True:
    c=0
    t1=0
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            c+=1
    if c==0:
        t1=n
        break
    else:
        n+=1
while True:
    c1=0
    t2=0
    for j in range(t,0,-1):
        if t%j==0:
            c1+=1
    if c1==2:
        t2=t
        break
    else:
        t-=1
if t1-f>=f-t2:
    print(f-t2)
elif t1-f<f-t2:
    print(t1-f)