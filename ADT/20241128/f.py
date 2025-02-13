from collections import defaultdict

N, M, H, K = map(int, input().split())
S = input()
d = defaultdict(int)
for _ in range(M):
    x, y = map(int, input().split())
    d[x, y] += 1
nx, ny = 0, 0
ans = "Yes"
for i in range(N):
    if S[i] == "R":
        nx += 1
    elif S[i] == "L":
        nx -= 1
    elif S[i] == "U":
        ny += 1
    elif S[i] == "D":
        ny -= 1
    H -= 1
    if H < 0:
        ans = "No"
        break
    if d[nx, ny] > 0 and H < K:
        d[nx, ny] -= 1
        H = K
print(ans)
