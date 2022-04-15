a,b=map(int,input().split())

def func(k):

    p=k%4
    re=0
    if p==0:
        re=k
    elif p==1:
        re=1
    elif p==2:
        re=k^1
    elif k==-1:
        re=0
    return re

ans=func(a-1)^func(b)
print(ans)
