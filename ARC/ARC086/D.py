N = int(input())
A = list(map(int, input().split()))
M = max(A)
m = min(A)
idx_M = A.index(M)
idx_m = A.index(m)
ans = []
if abs(M) >= abs(m):
    for i in range(N):
        if i == idx_M:
            continue
        A[i] += A[idx_M]
        ans.append((idx_M, i))
    A[0] += A[idx_M]
    ans.append((idx_M, 0))
    for i in range(N - 1):
        A[i + 1] += A[i]
        ans.append((i, i + 1))
else:
    for i in range(N):
        if i == idx_m:
            continue
        A[i] += A[idx_m]
        ans.append((idx_m, i))
    A[-1] += A[idx_m]
    ans.append((idx_m, N - 1))
    for i in range(N - 1, 0, -1):
        A[i - 1] += A[i]
        ans.append((i, i - 1))
print(len(ans))
for x, y in ans:
    print(x + 1, y + 1)
