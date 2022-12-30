
def solve(N, T):
    INF = 1 << 62
    dp = [INF]*(1 << N)
    dp[0] = 0
    cost = [[INF]*(1 << N) for _ in range(N)]
    for v in range(N):
        cost[v][0] = T[v][0]
    for v in range(N):
        for s in range(1 << N):
            cost[v][s]

    for s in range(1 << N):
        for v in range(N):
            if s & (1 << v):
                continue
            cost = T[v][0]
            for u in range(N):
                if s & (1 << u):
                    cost = min(cost, T[v][u+1])
            dp[s | (1 << v)] = min(dp[s | (1 << v)], dp[s]+cost)
    return dp[-1]


ans = []
while True:
    N = int(input())
    if N == 0:
        print(*ans, sep="\n")
        exit()
    T = [list(map(int, input().split())) for _ in range(N)]
    ans.append(solve(N, T))
N = int(input())
print(solve(N, T))
