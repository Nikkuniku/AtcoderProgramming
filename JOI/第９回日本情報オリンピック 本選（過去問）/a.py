from collections import defaultdict
N, M = map(int, input().split())
d = defaultdict(int)
for i in range(1, N):
    d[i] = d[i-1]+int(input())
ans = 0
MOD = 100000
now = 0
for _ in range(M):
    next = now+int(input())
    ans += abs(d[next]-d[now])
    ans %= MOD
    now = next
print(ans)
