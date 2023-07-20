from bisect import bisect_right
N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]
scores = [0]*N
for i in range(N):
    for j in range(3):
        scores[i] += P[i][j]
S = sorted(scores)
ans = []
for i in range(N):
    s = scores[i]
    idx = bisect_right(S, s+300)
    res = 'No'
    if N-K+1 <= idx:
        res = 'Yes'
    ans.append(res)
print(*ans, sep="\n")