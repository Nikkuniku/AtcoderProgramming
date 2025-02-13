N, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]
C.sort(key=lambda x: x[0], reverse=True)
w = 0
ans = 0
for i in range(N):
    a, b = C[i]
    if w + b <= W:
        ans += a * b
        w += b
    else:
        ans += a * min(b, (W - w))
        w += min(b, (W - w))
print(ans)
