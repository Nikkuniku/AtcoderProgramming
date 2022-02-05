n=int(input())
a=list(map(int,input().split()))

ans=a[0]
for i in range(1,n):
    if a[i]>ans:
        ans=a[i]
    else:
        break

print(ans)
