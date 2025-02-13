N = int(input())
A = list(map(int, input().split()))
C = [[] for _ in range(N + 1)]
for i, v in enumerate(A):
    C[v].append(i)
ans = 0
for v in range(1, N + 1):
    i, j = C[v][0], C[v][1]
    if abs(i - j) == 2:
        ans += 1
print(ans)
