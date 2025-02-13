from heapq import heappop, heappush

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)


def f(i, j, k):
    return A[i] * B[j] + B[j] * C[k] + C[k] * A[i]


ans = []
q = [(-f(0, 0, 0), 0, 0, 0)]
seen = set([(0, 0, 0)])


def add(i, j, k):
    if (i, j, k) in seen:
        return
    if i >= len(A):
        return
    if j >= len(B):
        return
    if k >= len(C):
        return
    heappush(q, (-f(i, j, k), i, j, k))
    seen.add((i, j, k))


for _ in range(K):
    val, i, j, k = heappop(q)
    add(i + 1, j, k)
    add(i, j + 1, k)
    add(i, j, k + 1)
    ans.append(-val)
print(ans[-1])
