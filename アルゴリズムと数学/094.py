n=int(input())
b=list(map(int,input().split()))

ans=0
for i in range(n):
    if i==0 :
        ans+=b[i]
    elif i==n-1:
        ans+=b[-1]
    else:
        ans+=min(b[i-1],b[i])
print(ans)