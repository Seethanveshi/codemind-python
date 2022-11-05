n=int(input())
l=list(map(int,input().split()))
s1,s2=0,0
for i in range(len(l)):
    if i<len(l)//2:
        s1+=l[i]
    else:
        s2+=l[i]
print(s1)
print(s2)