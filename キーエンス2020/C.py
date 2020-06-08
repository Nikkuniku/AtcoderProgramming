n,k,s = map(int,input().split())

ans=[]

cnt=n-k
for i in range(k):
    ans.append(s)

for j in range(cnt):
    if s==1:
        ans.append(2)
    elif s==10**9:
        ans.append((10**9)-1)
    else:
        ans.append(s+1)


print(*ans)