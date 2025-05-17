from collections import deque

N = int(input())
S = input()
q = deque()
for s in S:
    if q:
        if q[-1] == "(" and s == ")":
            q.pop()
            continue
    q.append(s)
ans = "No" if q else "Yes"
print(ans)
