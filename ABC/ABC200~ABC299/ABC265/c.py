h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
ans = [[False]*w for _ in range(h)]
x = 0
y = 0
ansx = -1
ansy = -1
while True:
    if ans[x][y]:
        print(-1)
        exit()

    if grid[x][y] == 'R':
        if y < w-1:
            ans[x][y] = True
            y += 1
        else:
            ansx = x
            ansy = y
            break
    elif grid[x][y] == 'D':
        if x < h-1:
            ans[x][y] = True
            x += 1
        else:
            ansx = x
            ansy = y
            break
    elif grid[x][y] == 'L':
        if 0 < y:
            ans[x][y] = True
            y -= 1
        else:
            ansx = x
            ansy = y
            break
    else:
        if 0 < x:
            ans[x][y] = True
            x -= 1
        else:
            ansx = x
            ansy = y
            break
print(ansx+1, ansy+1)
