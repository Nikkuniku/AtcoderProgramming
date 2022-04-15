h, w, a, b = map(int, input().split())

ans = [['0']*w for _ in range(h)]

p = max(a, w-a)
q = max(b, h-b)
for i in range(h):
    if i <= q-1:
        for j in range(p):
            ans[i][j] = '1'
    else:
        for j in range(p, w):
            ans[i][j] = '1'

for k in range(h):
    print(''.join(ans[k]))
