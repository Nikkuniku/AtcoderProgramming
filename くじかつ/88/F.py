n,m=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
mod=(10**9) + 7 

X = abs(x[n-1]-x[0])%mod
Y = abs(y[m-1]-y[0])%mod
K = pow(2,n+m-4,mod)

a=(X*Y)%mod
b=K%mod
print((a*b)%mod)