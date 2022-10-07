n=int(input())
l=[]
s=()
for i in str(n):
    l.append(i)
t=len(l)
t1=len(set(l))
if t==t1:
    print("Unique Number")
else:
    print("Not Unique Number")