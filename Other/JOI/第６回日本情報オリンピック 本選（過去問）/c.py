from collections import defaultdict
while 1:
    N = int(input())
    if N == 0:
        exit()
    S = defaultdict(lambda: False)
    Points = []
    for _ in range(N):
        a, b = map(int, input().split())
        Points.append((a, b))
        S[(a, b)] = True
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            xa, ya = Points[i]
            xc, yc = Points[j]
            xb = ((xa+xc)/2)+((yc-ya)/2)
            yb = ((ya+yc)/2)-((xc-xa)/2)
            xd = ((xa+xc)/2)-((yc-ya)/2)
            yd = ((ya+yc)/2)+((xc-xa)/2)
            if xb.is_integer() and yb.is_integer() and xd.is_integer() and yd.is_integer():
                xb = int(xb)
                yb = int(yb)
                xd = int(xd)
                yd = int(yd)
                if S[(xb, yb)] and S[(xd, yd)]:
                    tmp = ((xc-xa)**2 + (yc-ya)**2)/2
                    if tmp.is_integer():
                        ans = max(ans, int(tmp))
    print(ans)
