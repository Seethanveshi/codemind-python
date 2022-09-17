n=int(input())
t=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if t==s:
    print("True")
else:
    print("False")
