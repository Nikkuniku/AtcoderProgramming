N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(list(map(int, input().split())))
X = int(input())

dp = [False]*(X+1)
dp[0] = True
for i in range(X):
    for j in range(N):
        if i in B:
            continue
        if i+A[j] <= X:
            if i+A[j] in B:
                continue
            dp[i+A[j]] |= dp[i]
ans = 'No'
if dp[X]:
    ans = 'Yes'
print(ans)
