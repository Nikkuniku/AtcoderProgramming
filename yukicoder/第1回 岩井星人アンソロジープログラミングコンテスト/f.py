from collections import deque

S = input()[::-1]
q = deque()
ans = 0
for s in S:
    q.appendleft(s)
    while len(q) >= 3:
        if q[-3] == "1" and q[-2] == "1" and q[-1] == "0":
            q.pop()
            q.pop()
            q.pop()
            q.append("0")
            ans += 1
        else:
            break
print(ans)
