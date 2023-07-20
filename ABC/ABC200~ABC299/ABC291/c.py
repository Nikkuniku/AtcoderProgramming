from collections import defaultdict
N = int(input())
S = input()
d = defaultdict(lambda: False)
d[(0, 0)] = True
nx, ny = 0, 0
ans = 'No'
for i in range(N):
    s = S[i]
    if s == 'R':
        nx += 1
    elif s == 'L':
        nx -= 1
    elif s == 'U':
        ny += 1
    else:
        ny -= 1
    if d[(nx, ny)]:
        ans = 'Yes'
    d[(nx, ny)] = True
print(ans)
