N = int(input())
A = list(map(int, input().split()))
C = [[] for _ in range(N)]
for i, v in enumerate(A):
    C[v - 1].append(i)
ans = 0
for v in range(N):
    i, j = C[v][0], C[v][1]
    ans += abs(i - j) == 2
print(ans)
