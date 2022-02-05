n,k=map(int,input().split())

ans=n**3
for a in range(1,n+1):
    p=max(1,a-k+1)
    q=min(n,a+k-1)
    for b in range(p,q+1):
        for c in range(p,q+1):
            if abs(b-c)<k:
                ans-=1

print(ans)