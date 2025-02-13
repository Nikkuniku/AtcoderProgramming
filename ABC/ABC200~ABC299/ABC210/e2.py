from math import gcd

N, M = map(int, input().split())
Edge = [list(map(int, input().split())) for _ in range(M)]
Edge.sort(key=lambda x: x[1])
conn = N
ans = 0
for a, c in Edge:
    next = gcd(conn, a)
    ans += c * (conn - next)
    conn = next
if conn > 1:
    ans = -1
print(ans)
