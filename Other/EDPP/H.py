h,w=map(int,input().split())
a=[]

for _ in range(h):
    a.append(list(input()))

dp=[[0]*w for _ in range(h)]
dp[0][0]=1
for i in range(1,h):
    if a[i][0]=='.':
        dp[i][0]=1
    else:
        break

for j in range(1,w):
    if a[0][j]=='.':
        dp[0][j]=1
    else:
        break

for i in range(1,h):
    for j in range(1,w):
        if a[i][j]==".":
            if a[i-1][j]=="." and a[i][j-1]==".":
                dp[i][j]=dp[i][j-1]+dp[i-1][j]  
            elif a[i-1][j]=="." and a[i][j-1]=="#":
                dp[i][j]=dp[i-1][j]
            elif a[i-1][j]=="#" and a[i][j-1]==".":
                dp[i][j]=dp[i][j-1]
            else:
                dp[i][j]=0

# print(*a,sep="\n")
# print(*dp,sep="\n")

mod=10**9 + 7

print(dp[h-1][w-1]%mod)