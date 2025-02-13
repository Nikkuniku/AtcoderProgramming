A, B, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
ans = min(X) + min(Y)
for _ in range(M):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    tmp = X[x] + Y[y] - c
    ans = min(ans, tmp)
print(ans)
