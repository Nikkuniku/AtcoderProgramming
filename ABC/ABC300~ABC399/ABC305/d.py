from bisect import bisect_right
N = int(input())
A = list(map(int, input().split()))
cum = [0]
for i in range(1, N):
    if i % 2 != 0:
        cum.append(cum[-1])
    else:
        cum.append(cum[-1]+A[i]-A[i-1])


def solve(X):
    idx = bisect_right(A, X)-1
    res = -1
    if idx % 2 == 0:
        res = cum[idx]
    else:
        res = cum[idx]+X-A[idx]
    return res


Q = int(input())
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    tmp = solve(r)-solve(l)
    ans.append(tmp)
print(*ans, sep="\n")
