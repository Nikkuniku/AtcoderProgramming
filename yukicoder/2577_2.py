N = int(input())
fa = [1] * (N + 1)
for i in range(N):
    fa[i + 1] = fa[i] * (i + 1)


def P(n, k):
    """
    長さnの順列としてありうるもので、辞書順でk番目のもの
    """
    S = list(range(n))
    res = []
    for i in range(1, n + 1):
        a = fa[n - i]
        j = k // a
        res.append(S[j] + 1)
        S = S[:j] + S[j + 1 :]
        k %= a
    return res


l = 0
r = fa[N]
while r - l > 1:
    mid = (l + r) // 2
    Q = P(N, mid)
    print("?", *Q, flush=True)
    ret = int(input())
    if ret == 1:
        l = mid
    else:
        r = mid
print("!", *P(N, l), flush=True)
