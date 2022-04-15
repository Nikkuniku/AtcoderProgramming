n,m=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
a=list(reversed(a))
c=list(reversed(c))

ans=[]
for i in range(m+1):
    k=c[i]//a[0]
    for j in range(n+1):
        c[i+j]-=a[j]*k
    ans.append(k)

print(*reversed(ans))