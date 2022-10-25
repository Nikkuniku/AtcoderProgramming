X, K = map(int, input().split())
for i in range(K):
    for j in range(i):
        X //= 10
    p = X % 10
    X //= 10
    if p >= 5:
        X += 1
    X *= 10
    for j in range(i):
        X *= 10
print(X)
