def prime(n):
    p = True
    if n<2:
        p = False
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            p=False
            break
    return p
n=int(input())
s=0
for i in str(n):
    s+=1
p=prime(n)
if p==True:
    l=[]
    while n>0:
        r=n%10
        if prime(r)==True:
            l.append(r)
        else:
            print("Not Mega Prime")
            break
        n=n//10
    if s==len(l):
        print("Mega Prime")
else:
    print("Not Mega Prime")