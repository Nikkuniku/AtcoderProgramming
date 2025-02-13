from sys import setrecursionlimit

setrecursionlimit(10**9)
N, M = map(int, input().split())

ans = []


def rec(N, M, A=[]):
    if len(A) == N:
        ans.append(tuple(A))
        return
    a = 1 if len(A) == 0 else A[-1] + 10
    for b in range(a, M + 1):
        if b + (N - len(A) - 1) * 10 > M:
            continue
        A.append(b)
        rec(N, M, A)
        A.pop()
    return


rec(N, M)
print(len(ans))
for c in ans:
    if len(c) == N:
        print(*c)
