n,k=map(int,input().split())

r=list(map(int,input().split()))

r=sorted(sorted(r,reverse=True)[:k])

ans=0
for i in range(len(r)):
    ans+=r[i]
    ans/=2

print(ans)


