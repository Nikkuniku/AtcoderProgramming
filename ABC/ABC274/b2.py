h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]

ans = []
for col in zip(*grid):
    ans.append(col.count('#'))
print(*ans)
