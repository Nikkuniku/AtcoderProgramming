N = int(input())
A = list(map(int, input().split()))
MSB = [-1]*N
for i in range(N):
    for j in range(30):
        if (A[i] >> j) & 1:
            MSB[i] = max(MSB[i], j)
M = max(MSB)
B = []
for i, v in enumerate(MSB):
    if v == M:
        B.append(A[i])
K = len(B)
ans = 0
for j in range(30):
    tmp = 0
    for i in range(K):
        if (B[i] >> j) & 1:
            tmp += 1
    if tmp == 0 or tmp == K:
        continue
    ans += 1 << j
if K < N:
    ans += 1 << M
print(ans)
