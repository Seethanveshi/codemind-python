def nearest_fibonacci1(n):
    a=0
    b=1
    while True:
        if n<=a or n<=b:
            break
        a=a+b
        b=a+b
    if n==a or n==b:
        l1.append(n)
def nearest_fibonacci2(n):
    a=0
    b=1
    while True:
        if n<=a or n<=b:
            break
        a=a+b
        b=a+b
    if n==a or n==b:
        l2.append(n)
l1=[]
l2=[]
n=int(input())
for i in range(1,n+1,1):
    nearest_fibonacci1(i)
for j in range(n,n*2,1):
    nearest_fibonacci2(j)
if n-max(l1)<min(l2)-n:
    print(max(l1))
elif n-max(l1)>min(l2)-n:
    print(min(l2))
else:
    print(max(l1),min(l2))