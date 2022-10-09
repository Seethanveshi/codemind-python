n=int(input())
c=0
t=n*n
for i in str(n):
    c+=1
s=t%(10**c)
if n==s:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")