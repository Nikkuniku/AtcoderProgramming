from collections import deque

N = int(input())
S = input()
pre = ""
ans = 1
MOD = 1000000007
q = deque()
for s in S:
    if s != pre:
        q.append(s)
    else:
        m = len(q)
        ans *= (m + 1) // 2
        ans %= MOD
        while q:
            q.pop()
        q.append(s)
    pre = s
if q:
    m = len(q)
    ans *= (m + 1) // 2
    ans %= MOD
print(ans)
