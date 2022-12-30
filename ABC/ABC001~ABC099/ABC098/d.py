n=int(input())
a=list(map(int,input().split()))
ans=0
xorsum=0
csum=0
right=0
for left in range(n):
    while right<n and csum+a[right]==xorsum|a[right]:
        csum+=a[right]
        xorsum^=a[right]
        right+=1
    ans+=right-left
    if left==right:
        right+=1
    else:
        csum-=a[left]
        xorsum^=a[left]
print(ans)