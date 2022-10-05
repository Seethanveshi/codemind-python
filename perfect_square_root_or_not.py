n1=int(input())
c=0
for i in range(1,n1//2,1):
    if i*i==n1:
        c+=1
if c==0:
    print("False")
else:
    print("True")