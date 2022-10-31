n=int(input())
lst=list(map(int,input().split()))
s,l=0,0
for i in lst:
    s+=i
l=len(lst)
print("{0:.2f}".format(s/l))