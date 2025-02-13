h, m = map(int, input().split())
Lim = 60 * 18
now = 60 * h + m
ans = Lim - now
print(ans)
