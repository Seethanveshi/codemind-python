n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    for j in range(i+2,len(l),1):
        if l[i]%2==0 and l[j]%2!=0 and j-i==2 or l[i]%2!=0 and l[j]%2==0 and j-i==2:
            c+=1
print(c)