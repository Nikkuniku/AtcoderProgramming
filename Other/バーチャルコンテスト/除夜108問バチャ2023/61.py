from collections import Counter
N, K = map(int, input().split())
S = [input() for _ in range(N)]
ans = 0
for i in range(1 << N):
    c = Counter('')
    for j in range(N):
        if i & (1 << j):
            c += Counter(S[j])
    ans = max(ans, list(c.values()).count(K))
print(ans)
