h,sn,sp=map(int,input().split())
if h>50 and sn>60 and sp>100:
    g=10
elif h>50 and sn>60:
    g=9
elif sn>60 and sp>100:
    g=8
elif h>50 and sp>100:
    g=7
elif h>50 or sn>60 or sp>100:
    g=6
else:
    g=5
print(g)