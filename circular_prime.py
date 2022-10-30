def prime(n):
    p="True"
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            p="False"
    if p=="True":
        p="True"
    else:
        p="False"
    return p
n=int(input())
p=prime(n)
if p=="True":
    n1=n
    rev=0
    while n1>0:
        r=n1%10
        rev=rev*10+r
        n1=n1//10
    if p==prime(rev):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")