N, M = map(int, input().split())
S = set(list(map(int, input().split())))
X = []
for v in range(1, N + 1):
    if v not in S:
        X.append(v)
print(len(X))
print(*X)
