n,k=map(int,input().split())
a=list(map(int,input().split()))

s=sum(a)
ans='No'
if s<=k:
    if (k-s)%2==0:
        ans='Yes'
print(ans)