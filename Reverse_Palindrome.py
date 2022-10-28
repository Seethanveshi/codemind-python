def rev(x):
    rev=0
    while x>0:
        r=x%10
        rev=rev*10+r
        x=x//10
    return rev
x=int(input())
while True:
    x=x+rev(x)
    if x==rev(x):
        print(x)
        break