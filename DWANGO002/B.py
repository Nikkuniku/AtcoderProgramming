n=int(input())
k=list(map(int,input().split()))

ans=[]

ans.append(k[0])

for i in range(n-2):
    pre = k[i]
    pos = k[i+1]
    if pre<=pos:
        if ans[i]<pre:
            ans.append(pre)
        else:
            ans.append(k[i])
    else:
        ans.append(k[i+1])

ans.append(k[-1])

print(*ans)
