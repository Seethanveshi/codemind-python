n=int(input())
t=n**2
s=0
while t>0:
    r=t%10
    s+=r
    t=t//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")