n=int(input())
st=str(n)
l=list(st)
l2=[]
for i in l:
    s=1
    for j in range(int(i),0,-1):
        s*=j
    l2.append(s)
t=sum(l2)
if n==t:
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")