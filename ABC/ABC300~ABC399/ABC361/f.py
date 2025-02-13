N = int(input())
L = 60
ans = [0] * L
for b in range(L - 1, 1, -1):
    l = 0
    r = 1 << 60
    while r - l > 1:
        mid = (l + r) // 2
        if mid**b > N:
            r = mid
        else:
            l = mid
    ans[b] = l - 1
    d = 2 * b
    while d < L:
        ans[b] -= ans[d]
        d += b
print(sum(ans) + 1)
