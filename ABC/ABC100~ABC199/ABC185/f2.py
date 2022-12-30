n,q=map(int,input().split())
a=list(map(int,input().split()))
BIT=[0]*(n+1)

def add(i,x):
    idx=i
    while idx<len(BIT):
        BIT[idx]^=x
        idx+=(idx&-idx)

def sum(i):
    idx=i
    s=0
    while idx>0:
        s^=BIT[idx]
        idx-=(idx&-idx)
    return s
for i in range(n):
    add(i+1,a[i])
ans=[]
for _ in range(q):
    c,x,y=map(int,input().split())
    if c==1:
        add(x,y)
    else:
        ans.append(sum(y)^sum(x-1))
    
print(*ans,sep="\n")