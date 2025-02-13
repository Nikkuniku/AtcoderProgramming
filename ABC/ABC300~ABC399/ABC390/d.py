N = int(input())
A = list(map(int, input().split()))
dp = [[set() for _ in range(N + 1)] for _ in range(1 << N)]
for s in range(1, 1 << N):
    temp = 0
    for i in range(N):
        if s & (1 << i):
            temp += A[i]
    dp[s][1].add(temp)
    for j in range(2, N + 1):
        x = s
        while x > 0:
            for p in dp[s - x][j - 1]:
                for q in dp[x][1]:
                    dp[s][j].add(p ^ q)
            x = (x - 1) & s
ans = set()
for k in range(1, N + 1):
    ans |= dp[(1 << N) - 1][k]
print(len(ans))
print(sorted(ans))
