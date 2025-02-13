N, K = map(int, input().split())
A = list(map(int, input().split()))
l = -1
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    cnt = 0
    for a in A:
        cnt += max(a - mid + 1, 0)
    if cnt <= K:
        r = mid
    else:
        l = mid
ans = 0
cnt = 0
for a in A:
    if a >= r:
        ans += (a * (a + 1) // 2) - (r * (r - 1) // 2)
        cnt += max(a - r + 1, 0)
if r - 1 > 0:
    ans += (K - cnt) * (r - 1)
print(ans)
