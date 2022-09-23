tc=int(input())
for i in range(tc):
    n=int(input())
    s=0
    t=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if t==s:
        print("True")
    else:
        print("False")