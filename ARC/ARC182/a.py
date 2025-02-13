N, Q = map(int, input().split())
ans = 1
MOD = 998244353
res = [0] * Q
PV = [list(map(int, input().split())) for _ in range(Q)]
for j in range(Q):
    pj, vj = PV[j]
    for i in range(j):
        pi, vi = PV[i]
        if pi == pj and vi > vj:
            exit(print(0))
        if pi != pj and vi > vj:
            if pi < pj:
                if res[i] == 1 or res[j] == -1:
                    exit(print(0))
                res[i] = -1
                res[j] = 1
            elif pi > pj:
                if res[i] == -1 or res[j] == 1:
                    exit(print(0))
                res[i] = 1
                res[j] = -1
for v in res:
    if v == 0:
        ans *= 2
        ans %= MOD
print(ans)
