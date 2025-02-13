from collections import defaultdict

N, X = map(int, input().split())
W = [int(input()) for _ in range(N)]
W1 = W[: (N // 2)]
W2 = W[(N // 2) :]

M = len(W1)
d1 = defaultdict(int)
for i in range(1 << M):
    tmp = 0
    for j in range(M):
        if i & (1 << j):
            tmp += W1[j]
    d1[tmp] += 1
L = len(W2)
d2 = defaultdict(int)
for i in range(1 << L):
    tmp = 0
    for j in range(L):
        if i & (1 << j):
            tmp += W2[j]
    d2[tmp] += 1
ans = 0
for k, v in d1.items():
    ans += v * d2[X - k]
print(ans)
