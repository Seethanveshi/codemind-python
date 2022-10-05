n1=int(input())
n2=int(input())
s1=0
s2=0
for i in range(1,n1,1):
    if n1%i==0:
        s1+=i
for j in range(1,n2,1):
    if n2%j==0:
        s2+=j
if s1==n2 and s2==n1:
    print("Amicable")
else:
    print("Not Amicable")