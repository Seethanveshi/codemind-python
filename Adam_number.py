n=int(input())
s=0
s1=0
t=n**2
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
t1=s**2
while t1>0:
    r1=t1%10
    s1=s1*10+r1
    t1=t1//10
if t==s1:
    print("True")
else:
    print("False")