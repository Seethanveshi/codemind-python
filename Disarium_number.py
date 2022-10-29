def disarium_number(n):
    s=0
    j=1
    for i in str(n):
        s=(int(i))**j+s
        j+=1
    return s
n=int(input())
s=disarium_number(n)
if n==s:
    print("True")
else:
    print("False")