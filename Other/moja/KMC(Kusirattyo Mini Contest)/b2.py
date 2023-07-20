h, w = map(int, input().split())
S = []
for i in range(h):
    s = list(input())
    S.append(s)

ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def isvaild(x, y):
    return 0 <= x < h and 0 <= y < w


for i in range(h):
    for j in range(w):
        if(S[i][j] == "#"):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if(isvaild(nx, ny)):
                    if(S[nx][ny] == "."):
                        ans += 1
                else:
                    ans += 1

print(ans)
