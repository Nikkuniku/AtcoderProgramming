from collections import defaultdict
N, M, H, K = map(int, input().split())
S = input()
d = defaultdict(int)
for _ in range(M):
    x, y = map(int, input().split())
    d[x, y] = 1
ans = 'Yes'
nx, ny = 0, 0
hp = H
for i in range(N):
    s = S[i]
    if s == 'R':
        nx += 1
    elif s == 'L':
        nx -= 1
    elif s == 'U':
        ny += 1
    elif s == 'D':
        ny -= 1
    hp -= 1
    if hp < 0:
        ans = 'No'
        break
    if d[nx, ny] == 1 and hp < K:
        d[nx, ny] -= 1
        hp = K
print(ans)
