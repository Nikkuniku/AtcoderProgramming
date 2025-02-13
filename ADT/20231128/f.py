N, K = map(int, input().split())
A = list(map(int, input().split()))
gr = [[] for _ in range(K)]
for i, v in enumerate(A):
    gr[i % K].append(v)
for i in range(K):
    gr[i] = sorted(gr[i])
res = []
for i in range(N):
    res.append(gr[i % K][i // K])
ans = "No"
if res == sorted(res):
    ans = "Yes"
print(ans)
