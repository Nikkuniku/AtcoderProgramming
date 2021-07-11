n,p,q=map(int,input().split())
a=list(map(int,input().split()))

ans=0
for i in range(n):
    for j in range(i):
        for k in range(j):
            for l in range(k):
                for m in range(l):
                    if (a[i]%p*a[j]%p*a[k]%p*a[l]%p*a[m]%p)%p==q:
                        ans+=1

print(ans)