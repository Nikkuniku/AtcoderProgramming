N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())
ans = 1 << 60
for x in range(N + 1):
    y = ((E * N - H - (B + E) * x) // (D + E)) + 1
    if y < 0:
        y = 0
    tmp = A * x + C * y
    ans = min(ans, tmp)
print(ans)
