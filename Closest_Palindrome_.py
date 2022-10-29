def nearest_palindrome1(n):
        rev1=0
        n1=n
        while n1>0:
            r1=n1%10
            rev1=rev1*10+r1
            n1=n1//10
        if rev1==n:
            l1.append(n)
def nearest_palindrome2(n):
        rev2=0
        n2=n
        while n2>0:
            r2=n2%10
            rev2=rev2*10+r2
            n2=n2//10
        if rev2==n:
            l2.append(n)

l1=[]
l2=[]
n=int(input())
for i in range(1,n,1):
    nearest_palindrome1(i)
for j in range(n+1,n*2,1):
    nearest_palindrome2(j)
if n-max(l1)<min(l2)-n:
    print(max(l1))
elif n-max(l1)>min(l2)-n:
    print(min(l2))
else:
    print(max(l1),min(l2))