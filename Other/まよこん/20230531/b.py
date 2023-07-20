from collections import deque
S = list(input())
q = deque()
ans = 0
for i in range(len(S)):
    q.append(S[i])
    if len(q) > 1:
        v = q.pop()
        w = q.pop()
        ans += 2
        if v == w:
            q.append(v)
            q.append(w)
            ans -= 2
print(ans)
