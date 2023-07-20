n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

inf = float('inf')
dp = [[inf]*(m+1) for _ in range(n+1)]

dp[0][0] = 0
for i in range(1, n+1):
    for j in range(1, m+1):

        dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)

        if s[i-1] == t[j-1]:
            dp[i][j] = min(dp[i][j], dp[i-1][j-1])
        else:
            dp[i][j] = min(dp[i][j], dp[i-1][j-1]+1)

print(dp[n][m])

# print(*dp,sep="\n")

# for j in range(1,m+1):
#     for i in range(1,n+1):
#         if s[i-1]==t[j-1]:
#             # dp[i][j]=dp[i-1][j-1]
#             dp2[j][i]=min(dp2[j-1][i-1],dp2[j][i-1],dp2[j-1][i])
#         else:
#             dp2[j][i]=min(dp2[j][i],dp2[j][i-1]+1,dp2[j-1][i]+1,dp2[j-1][i-1]+1)

# # print(*dp,sep="\n")
# # print('---------')
# # print(*dp2,sep="\n")
# # print(dp[n][m])
# print(min(dp2[m][n],dp[n][m]))


# from collections import deque
# ans=deque([])

# while i>0 and j>0:
#     if dp[i][j]==dp[i-1][j-1]:
#         i-=1
#         j-=1
#     elif dp[i][j-1]==dp[i][j]:
#          j-=1
#     elif dp[i-1][j]==dp[i][j]:
#         i-=1
#     elif dp[i-1][j-1]<dp[i][j]:
#         ans.appendleft(s[i-1])
#         i-=1
#         j-=1

# print(dp[n][m])
