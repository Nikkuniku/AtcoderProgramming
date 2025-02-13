N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
ans = 1 << 60
for i in range(K + 1):
    temp = A[i + N - K - 1] - A[i]
    ans = min(ans, temp)
print(ans)
