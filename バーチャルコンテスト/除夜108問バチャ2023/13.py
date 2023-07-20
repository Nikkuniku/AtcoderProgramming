X, Y, N = map(int, input().split())

ans = 1 << 60
for y in range(200):
    tmp = Y*y
    if N-3*y >= 0:
        tmp += (N-3*y)*X
        ans = min(ans, tmp)
print(ans)
