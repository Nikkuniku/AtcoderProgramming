n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

INF=10**18
ans_a=[INF]*n
ans_b=[INF]*n
ans_a[-1]=a[-1]
ans_b[-1]=b[-1]
for i in range(n-2,-1,-1):
    p=a[i]
    q=b[i]
    if abs(p-ans_a[i+1])<=k or abs(p-ans_b[i+1])<=k:
        ans_a[i]=p
    if abs(q-ans_a[i+1])<=k or abs(q-ans_b[i+1])<=k:
        ans_b[i]=q

ans='Yes'
for i in range(n):
    if ans_a[i]==INF and ans_b[i]==INF:
        ans='No'
print(ans)