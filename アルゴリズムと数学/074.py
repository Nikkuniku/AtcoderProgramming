n=int(input())
a=list(map(int,input().split()))

ans=0
for k in range(n):
    ans+=(2*k-n+1)*a[k]
print(ans)
