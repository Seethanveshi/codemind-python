def prime(n):
    p=True
    for i in range(2,int(n**0.5)+1,1):
        if n%i==0:
            p=False
    return p
def palindrome(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
n+=1
while True:
    if prime(n)==True and palindrome(n)==n:
        print(n)
        break
    else:
        n+=1