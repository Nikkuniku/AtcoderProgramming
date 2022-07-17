h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(list(input()))
INF = 10**9
nums = [[INF]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            nums[i][j] = 0
# 右方向
for i in range(h):
    for j in range(1, w):
        nums[i][j] = min(nums[i][j], nums[i][j-1]+1)
# 左方向
for i in range(h):
    for j in range(w-2, -1, -1):
        nums[i][j] = min(nums[i][j], nums[i][j+1]+1)
# 下方向
for j in range(w):
    for i in range(1, h):
        nums[i][j] = min(nums[i][j], nums[i-1][j]+1)
# 上方向
for j in range(w):
    for i in range(h-2, -1, -1):
        nums[i][j] = min(nums[i][j], nums[i+1][j]+1)

ans = -1
for i in range(h):
    for j in range(w):
        ans = max(ans, nums[i][j])
print(ans)
