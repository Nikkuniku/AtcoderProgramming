from sys import setrecursionlimit

setrecursionlimit(10**8)
H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
ans = 0


def dfs(i, j, jewel):
    global ans
    if A[i][j] == "o":
        jewel += 1
    elif A[i][j] == "x":
        jewel -= 1
    else:
        return
    if jewel < 0:
        return
    if i == H - 1 and j == W - 1:
        ans += 1
        return

    if i + 1 < H:
        dfs(i + 1, j, jewel)
    if j + 1 < W:
        dfs(i, j + 1, jewel)


dfs(0, 0, 0)
print(ans)
