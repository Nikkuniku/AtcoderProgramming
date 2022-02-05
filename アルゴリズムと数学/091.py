n,x=map(int,input().split())

ans=0
for a in range(1,n):
    for b in range(a+1,n):
        for c in range(b+1,n):
            if a+b+c==n:
                ans+=1

print(ans)