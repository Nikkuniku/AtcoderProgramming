H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
isolates = [0]*H
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
OKNG = [0, 0]
UPDW = [0]*H
for i in range(H):
    for j in range(W):
        cnt = 0
        tmp = 0
        updw = 0
        leri = 0
        for k in range(4):
            ni = i+dx[k]
            nj = j+dy[k]
            if 0 <= ni < H and 0 <= nj < W:
                cnt += 1
                if A[i][j] != A[ni][nj]:
                    tmp += 1
                else:
                    if k % 2 == 0:
                        leri += 1
                    else:
                        updw += 1
        if cnt == tmp:
            isolates[i] += 1
        else:
            if leri == 0 and updw > 0:
                UPDW[i] += 1
    if isolates[i] > 0:
        if UPDW[i] > 0:
            OKNG[1] += 1
        else:
            OKNG[0] += 1
    else:
        OKNG[1] += 1

ans = 0
if sum(isolates) == 0:
    ans = 0
else:
    if OKNG[1] == H:
        ans = -1
    else:
        ans = min(OKNG)
print(ans)
