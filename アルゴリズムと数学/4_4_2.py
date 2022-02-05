def f(x):
    return 2**(x**2)

n=int(input())

ans=0
for i in range(1,n+1):
    ans+=f((2*i-1)/(2*n))
ans/=n

print(ans)