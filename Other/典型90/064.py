n,q=map(int,input().split())
a=list(map(int,input().split()))

b=[]
ans=0
for i in range(n-1):
    b.append(a[i+1]-a[i])
    ans+=abs(b[-1])

for _ in range(q):
    l,r,v=map(int,input().split())

    before =0
    after= 0
    if l>=2:
        before+=abs(b[l-2])
        b[l-2]+=v
        after+=abs(b[l-2])
    
    if r<=n-1:
        before+=abs(b[r-1])
        b[r-1]-=v
        after+=abs(b[r-1])

    dif = after-before
    ans+=dif
    print(ans)

