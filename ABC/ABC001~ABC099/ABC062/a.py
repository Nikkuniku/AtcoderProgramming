x, y = map(int, input().split())
g = [-1, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0]
ans = 'No'
if g[x] == g[y]:
    ans = 'Yes'
print(ans)
