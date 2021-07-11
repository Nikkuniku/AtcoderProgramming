n=int(input())
mod = 10**9 + 7
a=[]
for _ in range(n):
    p=list(map(int,input().split()))
    a.append(p)

ans=1
for i in range(n):
    ans*=sum(a[i])

print(ans%mod)