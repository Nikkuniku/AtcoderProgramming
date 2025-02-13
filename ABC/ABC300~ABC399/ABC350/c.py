N = int(input())
A = list(map(int, input().split()))
idxes = [-1] * (N + 1)
for i, v in enumerate(A):
    idxes[v] = i
ans = []
for v in range(1, N + 1):
    if idxes[v] == v - 1:
        continue
    i = idxes[v]
    w = A[v - 1]
    j = idxes[w]
    idxes[v], idxes[w] = j, i
    A[j], A[i] = v, w
    if j < i:
        i, j = j, i
    ans.append((i + 1, j + 1))
print(len(ans))
if ans:
    for c in ans:
        print(*c)
