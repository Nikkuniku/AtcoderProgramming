n=int(input())
a=list(map(int,input().split()))

ans=0
for i in range(n):
    tmp=a[i]
    for j in range(i,n):
        tmp = min(a[j],tmp)

        ans=max(ans,tmp*(j-i+1))

print(ans)

