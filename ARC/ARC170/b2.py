A = list(map(int, input().split()))
N = len(A)
res = set()
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[j] - A[i] == A[k] - A[j]:
                res.add((i + 1, k + 1))
res = sorted(list(res))
print(len(res))
print(*res, sep="\n")
