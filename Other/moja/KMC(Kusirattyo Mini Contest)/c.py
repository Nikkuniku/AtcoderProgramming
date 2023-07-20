def solve(H, W, sx, sy, gx, gy):
    if sx == gx or sy == gy:
        a = min(abs(sy-gy), W-abs(sy-gy))
        b = min(abs(sx-gx), H-abs(sx-gx))
        res = 2*(a+b)
    else:
        # gxに合わせる
        dx = min(abs(sx-gx), W-abs(sx-gx))
        (sy+dx)


T = int(input())
ans = []
for _ in range(T):
    Q = list(map(int, input().split()))
    ans.append(solve(*Q))
print(*ans, sep="\n")
