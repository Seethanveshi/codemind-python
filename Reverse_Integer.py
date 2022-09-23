n=int(input())
s=0
if n>0:
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    print(s)
elif n<0:
    t=-n
    while t>0:
        r=t%10
        s=s*10+r
        t=t//10
    print(-s)
    