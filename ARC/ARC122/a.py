n=int(input())
a=list(map(int,input().split()))

dp0=[0]
dp1=[0]
mod=10**9+7
x=0
y=1

for i in range(n):
    p=a[i]
    q=dp0[-1]
    r=dp1[-1]
    dp0.append(q+r+y*p)
    dp1.append(q-x*p)
    x,y=y,x+y

ans=(dp0[n]+dp1[n])%mod

print(ans)
