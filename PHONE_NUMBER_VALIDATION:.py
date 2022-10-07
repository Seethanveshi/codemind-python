n=int(input())
c=0
for i in str(n):
    c+=1
t=n%(10**9)
if t!=0 and c==10:
    print("Valid")
else:
    print("Invalid")