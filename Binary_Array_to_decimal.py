n=int(input())
l=list(map(int,input().split()))
j=len(l)-1
s=0
for i in l:
    s=s+i*pow(2,j)
    j-=1
print(s)