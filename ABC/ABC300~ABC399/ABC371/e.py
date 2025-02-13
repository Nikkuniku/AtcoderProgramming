from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
S = set()
B = []
L = 2 * 10**5
Idx = [[] for _ in range(L + 1)]
for i, v in enumerate(A):
    S.add(v)
    B.append(len(S))
    Idx[v].append(i)
for v in range(L + 1):
    Idx[v].append(N)
ans = 0
M = sum(B)
ans = 0
for i in range(N):
    ans += M
    p = A[i]
    j = bisect_right(Idx[p], i)
    M -= Idx[p][j] - i
print(ans)
