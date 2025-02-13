N, X = map(int, input().split())
ans = [0] * (X + 1)
AB = [list(map(int, input().split())) for _ in range(N)]
for j in range(1, X + 1):
    for a, b in AB:
        ans[j] = max(ans[j], max(b - abs(j - a), 0))
print(*ans[1:])
