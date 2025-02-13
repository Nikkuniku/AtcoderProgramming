N, T = map(int, input().split())
A = list(map(int, input().split()))
res = set()
for i in range(N):
    res.add(A[i] % T)
res = sorted(res)
dists = []
for i in range(len(res) - 1):
    dists.append(abs(res[i] - res[i + 1]))
dists.append(abs(res[0] + T - res[-1]))
X = sum(dists) - max(dists)
ans = (X + 1) // 2
print(ans)
