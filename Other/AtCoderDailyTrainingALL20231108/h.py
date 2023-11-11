N = int(input())
C = list(map(int, input().split()))
dp = [[0] * 9 for _ in range(N + 1)]
for i in range(N + 1):
    for j in range(9):
        if i - C[j] >= 0:
            tmp = dp[i - C[j]]
            tmp[j] += 1

print(dp)
