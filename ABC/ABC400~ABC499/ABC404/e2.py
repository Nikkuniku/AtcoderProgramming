N = int(input())
C = [0] + list(map(int, input().split()))
A = [0] + list(map(int, input().split()))
Edge = [[] for _ in range(N)]
INF = 1 << 60
dp = [INF] * N
for i in range(1, N):
    for j in range(1, C[i] + 1):
        if i - j < 0:
            continue
        Edge[i - j].append(i)
print(Edge)
for i in range(N - 1, -1, -1):
    if A[i] > 0:
        dp[i] = 0
        break
for i in range(N - 1, -1, -1):
    for j in Edge[i]:
        dp[i] = min(dp[i], dp[j] + 1)
print(dp)
