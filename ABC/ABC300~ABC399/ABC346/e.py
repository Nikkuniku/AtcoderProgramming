from collections import defaultdict

H, W, M = map(int, input().split())
Query = [list(map(int, input().split())) for _ in range(M)][::-1]
r = 0
c = 0
pattern = set()
Colors = defaultdict(int)
for t, a, x in Query:
    if (t, a) in pattern:
        continue
    if t == 1:
        Colors[x] += W - c
        r += 1
    elif t == 2:
        Colors[x] += H - r
        c += 1
    pattern.add((t, a))
ans = []
zero = H * W
for k, v in Colors.items():
    if k == 0 or v == 0:
        continue
    ans.append((k, v))
    zero -= v
if zero:
    ans.append((0, zero))
ans.sort()
print(len(ans))
for c in ans:
    print(*c)
