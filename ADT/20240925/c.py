def intersect(x, y, v, w):
    return max(x, v) < min(y, w)


a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())
ans = "No"
if intersect(a, d, g, j) and intersect(b, e, h, k) and intersect(c, f, i, l):
    ans = "Yes"
print(ans)
