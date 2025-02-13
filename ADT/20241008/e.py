N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 1 << 60
for i in range(K + 1):
    m = A[i]
    M = A[i + (N - K) - 1]
    ans = min(ans, M - m)
print(ans)
