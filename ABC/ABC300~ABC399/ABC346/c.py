N, K = map(int, input().split())
A = set(list(map(int, input().split())))
S = K * (K + 1) // 2
for a in A:
    if a <= K:
        S -= a
print(S)
