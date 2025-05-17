N, K = map(int, input().split())
S = input()
from collections import deque

q = deque()
for s in S:
    if q:
        if q[-1] == "(" and s == ")":
            q.pop()
            continue
    q.append(s)
ans = "No" if q else "Yes"
print(ans)
Q = deque()
cnt = 0
for s in S:
    if s == "(":
        Q.append(s)
        Q.append("1")
