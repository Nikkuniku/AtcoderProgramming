n = int(input())
inf = []
for _ in range(n):
    x, y, h = map(int, input().split())
    inf.append((x, y, h))

for cx in range(0, 101):
    for cy in range(0, 101):
        h_s = set()
        Flg = True
        for i in range(n):
            x, y, h = inf[i]
            if h > 0:
                h_s.add(h+abs(x-cx)+abs(y-cy))

        if len(h_s) == 1:
            h_tmp = list(h_s)[0]
            for i in range(n):
                x, y, h = inf[i]
                if max(h_tmp-abs(x-cx)-abs(y-cy), 0) != h:
                    Flg = False
                    break
            if Flg:
                print(cx, cy, h_tmp)
