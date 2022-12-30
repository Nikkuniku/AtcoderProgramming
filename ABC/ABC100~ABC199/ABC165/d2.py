a,b,n=map(int,input().split())
x=min(n,b-1)

ans=a*x//b -a*(x//b)
print(ans)