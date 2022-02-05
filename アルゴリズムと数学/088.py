a,b,c=map(int,input().split())
mod=998244353

ans=a*b*c*(a+1)*(b+1)*(c+1)//8
ans%=mod
print(ans)