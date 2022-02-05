n=int(input())

units=[1]*(n+1)

for i in range(2,n+1):
    j=0
    while i+j<=n:
        units[i+j]+=1
        j+=i

ans=0
for k in range(1,n+1):
    ans+=k*units[k]

print(ans)