from collections import defaultdict

blue = defaultdict(int)
red = defaultdict(int)
N = int(input())
for _ in range(N):
    s = input()
    blue[s] += 1
M = int(input())
for _ in range(M):
    t = input()
    red[t] += 1
ans = 0
for k, v in blue.items():
    tmp = v - red[k]
    ans = max(tmp, ans)
print(ans)
