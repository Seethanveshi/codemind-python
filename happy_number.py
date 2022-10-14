n=int(input())
s=0
while n>0:
    r=n%10
    s+=r**2
    n=n//10
    if n==0 and s==1 or s==7:
        print("True")
        break
    elif n==0 and s<9:
        print("False")
        break
    elif n==0:
        n=s
        s=0