N, C = map(int, input().split())
ans = 0
T = list(map(int, input().split()))
last = -(1 << 60)
for t in T:
    if t - last < C:
        continue
    ans += 1
    last = t
print(ans)
