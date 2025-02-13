from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
Ind = [[] for _ in range(N + 1)]
for i, v in enumerate(A):
    Ind[v].append(i)
Q = int(input())
ans = []
for _ in range(Q):
    L, R, X = map(int, input().split())
    R -= 1
    L -= 1
    cnt = bisect_right(Ind[X], R) - bisect_right(Ind[X], L - 1)
    ans.append(cnt)
print(*ans, sep="\n")
