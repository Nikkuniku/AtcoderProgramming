n=int(input())
ans=10**30
for b in range(100):
    a =n//pow(2,b)
    c=n-a*pow(2,b)
    ans=min(ans,a+b+c)
print(ans)