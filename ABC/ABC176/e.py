from collections import Counter
H, W, m = map(int, input().split())
hs = []
ws = []
for _ in range(m):
    h, w = map(int, input().split())
    hs.append(h)
    ws.append(w)
c_h = Counter(hs)
c_w = Counter(ws)

h_max = max(c_h.values())
Z_h = set()
for k, v in c_h.items():
    if v == h_max:
        Z_h.add(k)

w_max = max(c_w.values())
Z_w = set()
for k, v in c_w.items():
    if v == w_max:
        Z_w.add(k)
ans = h_max+w_max

tmp = 0
for i in range(m):
    h, w = hs[i], ws[i]
    if h in Z_h and w in Z_w:
        tmp += 1

if tmp == len(Z_h)*len(Z_w):
    ans -= 1
print(ans)
