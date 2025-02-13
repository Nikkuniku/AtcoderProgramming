from sortedcontainers import SortedSet

N, Q = map(int, input().split())
s_up = SortedSet([N])
s_left = SortedSet([N])
INF = 1 << 60
Y = [INF] * (N + 1)
X = [INF] * (N + 1)
Y[N] = N
X[N] = N
ans = (N - 2) ** 2
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        idx = s_up.bisect_right(x)
        tmp_y = Y[s_up[idx]]
        tmp = tmp_y - 1  # 増える白石
        s_up.add(x)
        Y[x] = tmp_y
        X[tmp_y] = min(X[tmp_y], x)
    elif t == 2:
        idx = s_left.bisect_right(x)
        tmp_x = X[s_left[idx]]
        tmp = tmp_x - 1
        s_left.add(x)
        X[x] = tmp_x
        Y[tmp_x] = min(Y[tmp_x], x)
    ans -= tmp - 1
print(ans)
