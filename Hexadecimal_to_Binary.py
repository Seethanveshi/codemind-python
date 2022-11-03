for _ in range(int(input())):
    n=int(input(),16)
    b = bin(n)[2:]
    if len(b)%4 != 0 :
        print('0'*(4 - len(b)%4)+b)
    else:
        print(b)