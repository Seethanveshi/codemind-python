n=int(input())
lst=list(map(int,input().split()))
s,l=0,0
for i in lst:
    s+=i
l=len(lst)
avg=s//l
if avg in lst:
    print("True")
else:
    print("False")