H,N=map(int,input().split())

#dp配列
# dp=[[float('inf')]*(H+1) for _ in range(N+1)]
# for j in range(H+1):
#     dp[0][j] =0

# for i in range(N):
#     A_i,B_i = map(int,input().split())
#     for a in range(H+1):
#         if A_i<=a:
#             dp[i+1][a] = min(dp[i][a-A_i] + B_i , dp[i][a])
#         else:
#             dp[i+1][a] = dp[i][a]

# print(*dp,sep="\n")

# print(dp[N][H])
dp = [float('inf')]*(H+1)
dp[0] = 0

for i in range(N):
    A_i,B_i = map(int,input().split())
    for j in range(H+1):
        nj = min(j+A_i,H)
        dp[nj] = min(dp[nj],dp[j] + B_i)
# print(*dp,sep="\n")
print(dp[H])