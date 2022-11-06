n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=[]
c1=0
for i in l:
    c=0
    for j in range(1,i+1,1):
        if i%j==0:
            c+=1
    if c==2:
        if i>=k:
            c1+=1
print(c1)