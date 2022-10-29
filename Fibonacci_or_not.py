def fibonacci(n):
    a=0
    b=1
    while True:
        a=a+b
        b=a+b
        if n==a or n==b:
            print("True")
            break
        elif n<a or n<b:
            print("False")
            break
n=int(input())
fibonacci(n)