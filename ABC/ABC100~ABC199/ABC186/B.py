h,w=map(int,input().split())
a=[]
tmp=float('inf')
for _ in range(h):
    b=list(map(int,input().split()))
    a.append(b)
    tmp=min(tmp,min(b))

ans=0
for i in range(h):
    for j in range(w):
        if a[i][j]>tmp:
            ans+=(a[i][j]-tmp)

print(ans)