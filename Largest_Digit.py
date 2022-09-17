n=int(input())
l=0
while n>0:
    r=n%10
    if r>l:
        l=r
    n=n//10
print(l)