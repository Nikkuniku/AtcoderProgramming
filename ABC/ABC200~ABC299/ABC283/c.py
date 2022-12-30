from collections import deque
S = input()
S = S[::-1]
q = deque(S)
ans = 0
while q:
    if len(q) >= 2:
        if q[0] == q[1] == '0':
            q.popleft()
            q.popleft()
        else:
            q.popleft()
        ans += 1
    else:
        q.popleft()
        ans += 1
print(ans)
