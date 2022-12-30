from collections import deque, defaultdict
n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())
s = set()
for _ in range(m):
    s.add(tuple(map(int, input().split())))
dp = defaultdict(int)
dp[(0, 0)] = 1
q = deque([(0, 0)])
ans = 0
MOD = 998244353
for i in range(n):
    L = len(q)
    for _ in range(L):
        x, y = q.popleft()

        if not (x+a, y+b) in s:
            dp[(x+a, y+b)] = (dp[(x+a, y+b)]+dp[(x, y)]) % MOD
            q.append((x+a, y+b))
            if i == n-1:
                ans += dp[(x+a, y+b)]
                ans %= MOD
        if not (x+c, y+d) in s:
            dp[(x+c, y+d)] = (dp[(x+c, y+d)]+dp[(x, y)]) % MOD
            q.append((x+c, y+d))
            if i == n-1:
                ans += dp[(x+c, y+d)]
                ans %= MOD
        if not (x+e, y+f) in s:
            dp[(x+e, y+f)] = (dp[(x+e, y+f)]+dp[(x, y)]) % MOD
            q.append((x+e, y+f))
            if i == n-1:
                ans += dp[(x+e, y+f)]
                ans %= MOD

print(ans)
