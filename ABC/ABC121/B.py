n,m,c =map(int,input().split())

b =list(map(int,input().split()))

ans=0
for _ in range(n):
    total =c

    a = list(map(int,input().split()))

    for i in range(m):
        total += a[i]*b[i]

    if total>0:
        ans+=1
    
print(ans)
