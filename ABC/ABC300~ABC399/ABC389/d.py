R = int(input())
ans = 0
for i in range(R):
    l = 0
    r = 2 * R
    while r - l > 1:
        mid = (l + r) // 2
        if (2 * mid + 1) ** 2 <= 4 * R * R - (2 * i + 1) ** 2:
            l = mid
        else:
            r = mid
    if i == 0:
        ans += 2 * (l + 1) - 1
    else:
        ans += 2 * (l + 1) - 1
        ans += 2 * (l + 1) - 1
print(ans)
