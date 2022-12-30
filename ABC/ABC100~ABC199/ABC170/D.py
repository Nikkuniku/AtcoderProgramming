n=int(input())
a=list(map(int,input().split()))

a=sorted(a)
m=max(a)
dp=[0]*(m+1)
d={}
cnt=0
for i in range(n):
    b=a[i]
    if b in d:
        d[b]+=1
        continue
    else:
        d[b]=1
    j=b
    while b<=m+b:
        if b>m:
            break
        dp[b]+=1
        b+=j
        


for i in a:
    if dp[i]==1 and d[i]==1:
        cnt+=1

print(cnt)