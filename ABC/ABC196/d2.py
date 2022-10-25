from sys import setrecursionlimit
h, w, A, B = map(int, input().split())
used = [[False]*w for _ in range(h)]
ans = 0
setrecursionlimit(10000000)


def dfs(x, y, a, b):
    '''
    Parameters
    ----------
    x : int
        現在いる行番号
    y : int
        現在いる列番号
    a:int
        畳の枚数
    b:int
        半畳の枚数
    '''
    pass
    # 右下に到着したとき
    if x == h-1 and y == w:
        global ans
        ans += (a == 0 and b == 0)
        return
    # 畳の外を出てしまった時
    if y == w:
        dfs(x+1, 0, a, b)
        return

    # その位置に畳が既に置かれている時
    if used[x][y]:
        dfs(x, y+1, a, b)

    # 畳を使う(横)
    if y < w-1 and (not used[x][y]) and (not used[x][y+1]):
        used[x][y] = True
        used[x][y+1] = True
        dfs(x, y+1, a-1, b)
        used[x][y] = False
        used[x][y+1] = False
    # 畳を使う(縦)
    if x < h-1 and (not used[x][y]) and (not used[x+1][y]):
        used[x][y] = True
        used[x+1][y] = True
        dfs(x, y+1, a-1, b)
        used[x][y] = False
        used[x+1][y] = False

    # 半畳を使う
    if not used[x][y]:
        used[x][y] = True
        dfs(x, y+1, a, b-1)
        used[x][y] = False


dfs(0, 0, A, B)
print(ans)
