n,x = map(int,input().split())
a=list(map(int,input().split()))

a=sorted(a)

ans= 0

for i in range(n-1):
    if x>=a[i]:
        ans+=1
        x-=a[i]
    else:
        break

if x==a[n-1]:
    ans+=1

print(ans)