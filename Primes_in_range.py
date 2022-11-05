def prime(n):
    p=True
    if n%2==0:
        p=False
    else:
        for i in range(2,int(n**0.5)+1,1):
            if n%i==0:
                p=False
                break
    return p
n=int(input())
m=int(input())
c=0
for j in range(n,m+1,1):
    if prime(j)==True:
        c+=1
print(c)