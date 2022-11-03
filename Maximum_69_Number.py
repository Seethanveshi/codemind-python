n=int(input())
l=[]
while n>0:
    r=n%10
    l.append(r)
    n=n//10
l.reverse()
for i in range(len(l)):
    if l[i]==6:
        l[i]=9
        break
s=0
for j in l:
    s=s*10+j
print(s)