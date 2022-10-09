n=int(input())
s=str(n)
t1=len(s)
t2=len(set(s))
if t1==t2:
    print("Unique Number")
else:
    print("Not Unique Number")