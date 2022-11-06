def sum_digits(n):
    s=0
    while n>0:
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input())
l=list(map(int,input().split()))
s1=0
for i in l:
    s1+=sum_digits(i)
print(s1)