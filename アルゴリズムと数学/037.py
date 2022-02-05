a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))


def cross(x, y):
    p = x[0]*y[1]-x[1]*y[0]
    if p == 0:
        return 0
    else:
        return p//abs(p)


ca = [a[0]-c[0], a[1]-c[1]]
cb = [b[0]-c[0], b[1]-c[1]]

da = [a[0]-d[0], a[1]-d[1]]
db = [b[0]-d[0], b[1]-d[1]]

ac = [c[0]-a[0], c[1]-a[1]]
ad = [d[0]-a[0], d[1]-a[1]]
bc = [c[0]-b[0], c[1]-b[1]]
bd = [d[0]-b[0], d[1]-b[1]]

# CとDはAとBを結ぶ直線で分割した領域上にそれぞれ分布するか
s = cross(ca, cb)*cross(da, db)
# AとBはCとDを結ぶ直線で分割した領域上にそれぞれ分布するか
t = cross(ac, ad)*cross(bc, bd)

ans = 'No'
if s < 0 and t <= 0:
    ans = 'Yes'
elif s <= 0 and t < 0:
    ans = 'Yes'
elif s == t == 0:
    if a[0] == b[0] == c[0] == d[0]:
        if a[1] > b[1]:
            a, b = b, a
        if c[1] > d[1]:
            c, d = d, c
        if max(a[1], c[1]) <= min(b[1], d[1]):
            ans = 'Yes'
    else:
        if a[0] > b[0]:
            a, b = b, a
        if c[0] > d[0]:
            c, d = d, c

        if max(a[0], c[0]) <= min(b[0], d[0]):
            ans = 'Yes'

print(ans)
