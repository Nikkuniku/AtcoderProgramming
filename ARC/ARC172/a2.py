H, W, N = map(int, input().split())
A = list(map(int, input().split()))


def TotalArea(A, r):
    res = 0
    for i in A:
        if i >= r:
            res += (1 << i) ** 2
    return res


ans = "Yes"
for r in range(26):
    Limit = (H // (1 << r)) * (W // (1 << r)) * (1 << r) ** 2
    tot = TotalArea(A, r)
    if tot > Limit:
        ans = "No"
print(ans)
