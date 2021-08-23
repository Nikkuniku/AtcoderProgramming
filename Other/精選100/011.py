n,m=map(int,input().split())
lights=[tuple(map(int,input().split())) for _ in range(m)]
P=list(map(int,input().split()))

ans=0
for i in range(1<<n):
    switch=[False]*n
    for j in range(n):
        if (i>>j)&1:
            switch[j]=True

    ons=0
    for k in range(m):
        l =lights[k][1:]
        p=P[k]
        tmp=0
        for o in l:
            if switch[o-1]:
                tmp+=1
        if tmp%2==p:
            ons+=1
    if ons==m:
        ans+=1
print(ans)
