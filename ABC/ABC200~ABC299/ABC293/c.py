# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ans = 0


def dfs(vx, vy, path):
    global ans
    if vx == H-1 and vy == W-1:
        path.append(A[vx][vy])
        ans += (len(set(path)) == H+W-1)
        path.pop()
    if vx+1 < H:
        path.append(A[vx][vy])
        dfs(vx+1, vy, path)
        path.pop()
    if vy+1 < W:
        path.append(A[vx][vy])
        dfs(vx, vy+1, path)
        path.pop()


dfs(0, 0, [])
print(ans)
