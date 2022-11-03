n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
l1=[]
for i in l:
    if i<a or i>b:
        l1.append(i)
print(sum(l1))