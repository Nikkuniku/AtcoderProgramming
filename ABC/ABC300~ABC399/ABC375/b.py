def dist(X, Y):
    return ((X[0] - Y[0]) ** 2 + (X[1] - Y[1]) ** 2) ** 0.5


N = int(input())
P = [[0, 0]]
for _ in range(N):
    p = list(map(int, input().split()))
    P.append(p)
P.append([0, 0])
ans = 0
for i in range(len(P) - 1):
    ans += dist(P[i], P[i + 1])
print(ans)
