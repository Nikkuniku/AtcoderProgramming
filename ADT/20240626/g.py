N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(list(map(int, input().split())))
X = int(input())
dp = [False] * (X + 1)
dp[0] = True
for i in range(X):
    if not dp[i]:
        continue
    for j in range(N):
        if i + A[j] <= X and i + A[j] not in B:
            dp[i + A[j]] |= dp[i]
ans = "No"
if dp[X]:
    ans = "Yes"
print(ans)
