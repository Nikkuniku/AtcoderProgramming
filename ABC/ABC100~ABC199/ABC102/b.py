N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        tmp = abs(A[i] - A[j])
        ans = max(ans, tmp)
print(ans)
