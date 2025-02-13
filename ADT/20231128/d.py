N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
idx = [-1] * K
for i in range(K):
    idx[i] = A[i]
ans = []
for l in L:
    l -= 1
    if idx[l] == N:
        continue
    if idx[l] + 1 in idx:
        continue
    idx[l] += 1
print(*idx)
