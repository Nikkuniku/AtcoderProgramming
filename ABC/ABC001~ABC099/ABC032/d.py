from bisect import bisect_right
N, W = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(N)]
maxV = max([v for v, _ in goods])
maxW = max([w for _, w in goods])
if N <= 30:
    # 半分全列挙
    List1 = goods[:N//2]
    List2 = goods[N//2:]
    val1 = []
    val2 = []
    M = len(List1)
    K = len(List2)
    for i in range(1 << M):
        tmp_v = 0
        tmp_w = 0
        for j in range(M):
            if i & (1 << j):
                tmp_v += List1[j][0]
                tmp_w += List1[j][1]
        val1.append((tmp_v, tmp_w))
    for i in range(1 << K):
        tmp_v = 0
        tmp_w = 0
        for j in range(K):
            if i & (1 << j):
                tmp_v += List2[j][0]
                tmp_w += List2[j][1]
        val2.append((tmp_v, tmp_w))
    val2.sort(key=lambda x: x[1])
    Weights = [w for _, w in val2]
    Values = [v for v, _ in val2]
    for i in range(1, len(Values)):
        Values[i] = max(Values[i], Values[i-1])
    ans = 0
    for v, w in val1:
        idx = bisect_right(Weights, W-w)
        if w+Weights[idx-1] <= W:
            tmp = v+Values[idx-1]
            ans = max(ans, tmp)
    print(ans)
elif maxW <= 1000:
    sumW = sum([w for _, w in goods])
    dp = [[0]*(sumW+1) for _ in range(N+1)]
    for i in range(N):
        v, w = goods[i]
        for j in range(sumW+1):
            # 取らない
            dp[i+1][j] = dp[i][j]
            # 取れるなら取る
            if j-w >= 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-w]+v)
    print(dp[N][min(W, sumW)])
elif maxV <= 1000:
    sumV = sum([v for v, _ in goods])
    INF = 1 << 60
    # i番目までの荷物で価値Vを達成するための重さの最小値
    dp = [[INF]*(sumV+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        v, w = goods[i]
        for j in range(sumV+1):
            # 取らない
            dp[i+1][j] = dp[i][j]
            # 取れるなら取る
            if j-v >= 0:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-v]+w)
    ans = max([v if dp[N][v] <= W else 0 for v in range(sumV+1)])
    print(ans)
