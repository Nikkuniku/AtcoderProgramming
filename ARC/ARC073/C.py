n,t=map(int,input().split())
a=list(map(int,input().split()))


ans=0

for i in range(n):
    if i==0:
        s=0
        l=a[i]+t
        continue

    if a[i]<=l:
        l=a[i]+t
    else:
        ans+=l-s
        s=a[i]
        l=a[i]+t


ans+=l-s
print(ans)