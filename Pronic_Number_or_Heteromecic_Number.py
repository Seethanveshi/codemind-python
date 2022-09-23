n=int(input())
for i in range(0,n//2+1,1):
    if i*(i+1)==n:
        print("YES")
        break
if i*(i+1)==n:
    pass
else:
    print("NO")