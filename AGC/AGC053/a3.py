N = int(input())
S = input()
A = list(map(int, input().split()))
M = [abs(A[i] - A[i + 1]) for i in range(N)]
m = min(M)
ans = [[0] * (N + 1) for _ in range(m)]
for j in range(N + 1):
    r = A[j] % m
    for i in range(m):
        ans[i][j] = A[j] // m
        if i < r:
            ans[i][j] += 1
print(len(ans))
for c in ans:
    print(*c)
