from collections import defaultdict
h, w = map(int, input().split())
d = defaultdict(int)
for _ in range(h):
    s = list(input())
    for i in range(w):
        d[s[i]] += 1
p = list(d.values())

if h % 2 == 0:
    H = h//2
else:
    H = (h+1)//2
if w % 2 == 0:
    W = w//2
else:
    W = (w+1)//2


ans = 'Yes'
for i in range(H):
    for j in range(W):
        p.sort()
        needs = 1
        notflg = True
        if h-1-i != i:
            needs *= 2
        if w-1-j != j:
            needs *= 2
        for k in range(len(p)):
            if p[k] >= needs:
                p[k] -= needs
                notflg = False
                break

        if notflg:
            ans = 'No'
            break
print(ans)
