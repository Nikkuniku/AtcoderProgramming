N = int(input())
S = [int(input()) for _ in range(N)]


def solve(A):
    M = len(A)
    q = []
    # ランレングス圧縮
    for i in range(M):
        b = A[i]
        if q:
            p, c = q[-1]
            if p == b:
                p, c = q.pop()
                c += 1
                q.append((p, c))
            else:
                q.append((b, 1))
        else:
            q.append((b, 1))
    res = []
    for p, c in q:
        if c >= 4:
            continue
        if res:
            if res[-1][0] == p and res[-1][1]+c >= 4:
                res.pop()
            else:
                res.append((p, c))
        else:
            res.append((p, c))
    return res


ans = 1 << 60
for i in range(N):
    colors = {1, 2, 3}
    colors.discard(S[i])
    for t in colors:
        T = S[:]
        T[i] = t
        res = solve(T)
        ans = min(ans, sum([c for _, c in res]))
print(ans)
