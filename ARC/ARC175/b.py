from collections import Counter, deque

N, A, B = map(int, input().split())
S = input()
q = deque()
for s in S:
    q.append(s)
    if len(q) > 1:
        if q[-2] == "(" and q[-1] == ")":
            q.pop()
            q.pop()
ans = 0
if q:
    C = Counter(q)
    x = C["("]
    y = C[")"]
    if x and y:
        t = min(x, y)
        ans += ((t + 1) // 2) * min(A, 2 * B)
        x -= t
        y -= t
    if x != y:
        if min(x, y) % 2 == 1:
            ans += (min(x, y) % 2) * min(A, 2 * B)
            x -= 1
            y -= 1
        ans += B * max(x, y) // 2
print(ans)
