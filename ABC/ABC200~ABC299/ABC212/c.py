from bisect import bisect_left

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=sorted(a)
b=sorted(b)

ans=10**9
for i in range(n):
    p=a[i]
    j=bisect_left(b,p)

    for k in [-1,0,1]:
        if 0<=j+k<=m-1:
            ans=min(ans,abs(p-b[j+k]))
print(ans)