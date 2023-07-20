from collections import defaultdict


def decide(lim):
    # 各数字の高さの決定
    i = 0
    j = 1
    high = defaultdict(int)
    h = 0
    cnt = 0
    while i <= lim:
        high[i] = h
        i += 1
        cnt += 1
        if cnt == j:
            cnt = 0
            j += 1
            h += 1
    return high


M = 30
N = M*(M+1)//2
B = [list(map(int, input().split()))+[-1]*(M-1-i) for i in range(M)]
d = defaultdict(lambda: -1)
for i in range(M):
    for j in range(M):
        if B[i][j] == -1:
            continue
        d[B[i][j]] = [i, j]


def judge(M):
    res = 0
    dxy = [(1, 0), (1, 1)]
    for i in range(M-1):
        for j in range(M):
            if B[i][j] == -1:
                break
            less = True
            for dx, dy in dxy:
                if B[i+dx][j+dy] == -1:
                    continue
                if B[i+dx][j+dy] < B[i][j]:
                    less = False
            if not less:
                res += 1
    return res


height = decide(N)
dxy_up = [(-1, -1), (-1, 0)]
dxy_side = [(0, -1), (0, 1)]
ans = []
for i in range(N):
    x, y = d[i]
    seen = set((x, y))
    cnt = 0
    for _ in range(10):
        for dx, dy in dxy_up:
            nx = x+dx
            ny = y+dy
            if nx == -1 or ny == -1:
                continue
            if B[nx][ny] == -1:
                continue
            if height[B[nx][ny]] == nx:
                continue
            if (nx, ny) in seen:
                continue
            B[nx][ny], B[x][y] = B[x][y], B[nx][ny]
            d[i] = [nx, ny]
            d[B[x][y]] = [x, y]
            ans.append([x, y, nx, ny])
            x, y = nx, ny
            seen.add((x, y))
            break
        else:
            for dx, dy in dxy_side:
                nx = x+dx
                ny = y+dy
                if nx == -1 or ny == -1:
                    continue
                # if ny == x:
                #     ny = 0
                # elif ny == -1:
                #     ny = nx
                if B[nx][ny] == -1:
                    continue
                if height[B[nx][ny]] == nx:
                    continue
                if (nx, ny) in seen:
                    continue
                B[nx][ny], B[x][y] = B[x][y], B[nx][ny]
                d[i] = [nx, ny]
                d[B[x][y]] = [x, y]
                ans.append([x, y, nx, ny])
                x, y = nx, ny
                seen.add((x, y))
                break
            else:
                break

    # if judge(M) == 0:
    #     break


# with open('test.txt', 'w', encoding='utf-8') as file:
#     file.write(str(len(ans))+"\n")
#     for c in ans:
#         tmp = [str(p) for p in c]
#         file.write(' '.join(tmp)+"\n")
print(len(ans))
for c in ans:
    print(*c)
