N, K = map(int, input().split())
Points = [list(map(int, input().split())) for _ in range(N)]
kouho = []
# 左下を探す
xl = 1 << 60
yu = 1 << 60
xr = 0
yh = 0
for x, y in Points:
    xl = min(xl, x)
    yu = min(yu, y)
    xr = max(xr, x)
    yh = max(yh, y)
# どこまで縮めるか
l = -1
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    cost = 0
    for x, y in Points:
        cost += max(x - (xl + mid), 0)
        cost += max(y - (yu + mid), 0)
    if cost <= K:
        r = mid
    else:
        l = mid
kouho.append(r)
# 左上どこまで縮めるか
l = -1
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    cost = 0
    for x, y in Points:
        cost += max(x - (xl + mid), 0)
        cost += max((yh - mid) - y, 0)
    if cost <= K:
        r = mid
    else:
        l = mid
kouho.append(r)
# 右下どこまで縮めるか
l = -1
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    cost = 0
    for x, y in Points:
        cost += max((xr - mid) - x, 0)
        cost += max(y - (yu + mid), 0)
    if cost <= K:
        r = mid
    else:
        l = mid
kouho.append(r)
# 右上どこまで縮めるか
l = -1
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    cost = 0
    for x, y in Points:
        cost += max((xr - mid) - x, 0)
        cost += max((yh - mid) - y, 0)
    if cost <= K:
        r = mid
    else:
        l = mid
kouho.append(r)
print(min(kouho))
