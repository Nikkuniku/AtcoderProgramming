def solve(N, K, Q):
    idx = [-1] * (N + 1)
    for i, v in enumerate(Q):
        idx[v] = i
    now = 1
    cnt = 0
    while now <= N:
        i_now = idx[now]
        if Q[now] == now:
            now += 1
            continue
        swap_target = Q[now]
        j_now = idx[swap_target]
        Q[now], Q[i_now] = Q[i_now], Q[now]
        idx[now], idx[swap_target] = j_now, i_now
        now += 1
        cnt += 1
    if cnt <= K:
        return True
    return False


T = int(input())
ans = []
for _ in range(T):
    N, K = map(int, input().split())
    Q = [0] + list(map(int, input().split()))
    res = "No"
    if solve(N, K, Q):
        res = "Yes"
    ans.append(res)
print(*ans, sep="\n")
