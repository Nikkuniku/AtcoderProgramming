X, K = map(int, input().split())
for i in range(K):
    X //= pow(10, i)
    m = X % 10
    if m >= 5:
        X += 10 - m
    else:
        X -= m
    X *= pow(10, i)
print(X)
