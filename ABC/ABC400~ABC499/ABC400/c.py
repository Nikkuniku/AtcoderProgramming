N = int(input())
L = 60
ans = 0
for a in range(1, 3):
    l = 0
    r = 1 << 60
    while r - l > 1:
        mid = (l + r) // 2
        if pow(2, a) * pow(mid, 2) <= N:
            l = mid
        else:
            r = mid
    ans += l
print(ans)
