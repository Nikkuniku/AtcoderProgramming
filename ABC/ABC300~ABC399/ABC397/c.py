N = int(input())
A = list(map(int, input().split()))
L = set()
dp = []
for i in range(N):
    L.add(A[i])
    dp.append(len(L))
R = set()
ep = []
for i in range(N - 1, -1, -1):
    R.add(A[i])
    ep.append(len(R))
ep = ep[::-1]
ans = -(1 << 60)
for i in range(N - 1):
    temp = dp[i] + ep[i + 1]
    ans = max(ans, temp)
print(ans)
