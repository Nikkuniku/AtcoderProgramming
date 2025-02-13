N, M, X, T, D = map(int, input().split())
H = [-1] * (N + 1)
for i in range(N, -1, -1):
    if X <= i <= N:
        H[i] = T
    else:
        H[i] = H[i + 1] - D
print(H[M])
