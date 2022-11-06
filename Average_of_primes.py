n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    c=0
    for j in range(1,i+1,1):
        if i%j==0:
            c+=1
    if c==2:
        l1.append(i)
print("{:.2f}".format(sum(l1)/len(l1)))