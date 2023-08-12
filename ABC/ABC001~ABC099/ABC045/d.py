from collections import defaultdict
H, W, N = map(int, input().split())
d = defaultdict(set)
black = set()
for _ in range(N):
    a, b = map(int, input().split())
    black.add((a, b))
for a, b in black:
    for dx in range(-2, 1):
        for dy in range(-2, 1):
            isOK = True
            na = a+dx
            nb = b+dy
            cnt = 0
            for i in range(3):
                ni = na+i
                if not 1 <= ni <= H:
                    isOK = False
                    break
                for j in range(3):
                    nj = nb+j
                    if not 1 <= nj <= W:
                        isOK = False
                        break
                    if (ni, nj) in black:
                        cnt += 1
            if isOK:
                d[cnt].add((na, nb))
ans = [0]*10
for k, v in d.items():
    ans[k] = len(v)
ans[0] = (H-2)*(W-2)-sum(ans[1:])
print(*ans, sep="\n")
