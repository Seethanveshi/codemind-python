tc=int(input())
for i  in range(tc):
    c=0
    n=int(input())
    for i in range(1,n,1):
        if i*i==n:
            c+=1
    if c>0:
        print("True")
    else:
        print("False")