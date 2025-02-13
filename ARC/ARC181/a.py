from sortedcontainers import SortedList


def solve(N, P):
    if P == sorted(P):
        return 0
    if P[0] == N and P[-1] == 1:
        return 3
    tmp = SortedList()
    for i in range(N):
        tmp.add(P[i])
        idx = tmp.bisect_right(i + 1)
        if idx == i + 1 and P[i] == i + 1:
            return 1
    return 2


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    ans.append(solve(N, P))
print(*ans, sep="\n")
