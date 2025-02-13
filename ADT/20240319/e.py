N, W = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
cheese.sort(reverse=True)
now = 0
ans = 0
for a, b in cheese:
    tmp = min(max(W - now, 0), b)
    now += tmp
    ans += a * tmp
print(ans)
