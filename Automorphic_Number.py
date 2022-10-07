n=int(input())
t=n*n
c=0
for i in str(n):
    c+=1
f=t%(10**c)
if f==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")