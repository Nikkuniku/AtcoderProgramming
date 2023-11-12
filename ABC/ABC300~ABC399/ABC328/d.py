from collections import deque

S = list(input())
q = deque()
for s in S:
    if len(q) >= 2:
        if q[-2] == "A" and q[-1] == "B" and s == "C":
            q.pop()
            q.pop()
            continue
    q.append(s)
print(*q, sep="")
