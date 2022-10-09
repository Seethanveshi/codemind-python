n,x=map(int,input().split())
c=0
for i in str(n):
    c+=1
t1=n%(10**x)
t2=n//(10**(c-x))
if t1-t2>0:
    print(t1-t2)
else:
    print(t2-t1)