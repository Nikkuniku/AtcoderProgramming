N, K = map(int, input().split())
S = K * (K + 1) // 2
A = set(list(map(int, input().split())))
for a in A:
    if 1 <= a <= K:
        S -= a
print(S)
