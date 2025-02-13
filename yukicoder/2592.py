N, Q, K = map(int, input().split())
A = list(map(int, input().split()))
cum = [0]
MOD = 2124717198126521419
for i, v in enumerate(A):
    tmp = cum[-1] + v * pow(K, i, MOD)
    cum.append(tmp)
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    tmp = (cum[r] - cum[l - 1]) % MOD
    res = "Yes"
    if tmp == 0:
        res = "No"
    ans.append(res)
print(*ans, sep="\n")
