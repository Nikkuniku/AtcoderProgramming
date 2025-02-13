from bisect import bisect_left

S = list(input())
Q = int(input())
K = list(map(int, input().split()))
N = len(S)
pow2 = [pow(2, i) for i in range(61)]
ans = []


def solve(k):
    p = (k + N - 1) // N
    q = k - (p - 1) * N
    res = S[q - 1]
    issame = 1
    while p > 2:
        idx = bisect_left(pow2, p)
        p -= pow2[idx - 1]
        issame ^= 1
    if p == 1:
        if issame:
            pass
        else:
            if res.upper() == res:
                res = res.lower()
            else:
                res = res.upper()
    elif p == 2:
        if issame:
            if res.upper() == res:
                res = res.lower()
            else:
                res = res.upper()
        else:
            pass
    return res


for ki in K:
    ans.append(solve(ki))
print(*ans)
