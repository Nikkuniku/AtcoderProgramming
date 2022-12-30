H, W = map(int, input().split())


def ceil(a, b):
    return -1 * (-a // b)


ans = []

for h in range(1, H):
    a = h*W

    # パターン1
    b = (H-h) * (W//2)
    c = (H-h)*ceil(W, 2)
    if b > 0 and c > 0:
        p = sorted([a, b, c])
        ans.append(p[-1]-p[0])
    # パターン2
    b = W*((H-h)//2)
    c = W*ceil(H-h, 2)
    if b > 0 and c > 0:
        p = sorted([a, b, c])
        ans.append(p[-1]-p[0])

for w in range(1, W):
    a = w*H

    # パターン1
    b = H * ((W-w)//2)
    c = H*ceil(W-w, 2)
    if b > 0 and c > 0:
        p = sorted([a, b, c])
        ans.append(p[-1]-p[0])
    # パターン2
    b = (W-w)*(H//2)
    c = (W-w)*ceil(H, 2)
    if b > 0 and c > 0:
        p = sorted([a, b, c])
        ans.append(p[-1]-p[0])
print(min(ans))
