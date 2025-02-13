N, M, K = map(int, input().split())
S = [list(input()) for _ in range(N)]


def f(s, t, p):
    cnt = [0] * 10
    for i in range(s, s + p):
        for j in range(t, t + p):
            cnt[int(S[i][j])] += 1
    R = sum(cnt)
    for v in range(10):
        tmp = cnt[v]
        if R - tmp <= K:
            return True
    return False


ans = 1
for k in range(1, min(N, M) + 1):
    for i in range(N - k + 1):
        for j in range(M - k + 1):
            if f(i, j, k):
                ans = max(ans, k)
print(ans)
