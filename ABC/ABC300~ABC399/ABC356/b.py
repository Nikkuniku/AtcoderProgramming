N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * M
for i in range(N):
    X = list(map(int, input().split()))
    for j, v in enumerate(X):
        B[j] += v
ans = "Yes"
for i in range(M):
    if B[i] < A[i]:
        ans = "No"
print(ans)
