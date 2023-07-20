from collections import deque
N = int(input())
S = list(input())
q = deque()
left = 0
for i in range(N):
    t = S[i]
    if t == '(':
        left += 1
        q.append(t)
    elif t == ')':
        q.append(t)
        if left > 0:
            while q[-1] != '(':
                q.pop()
            q.pop()
            left -= 1
    else:
        q.append(t)
ans = ''.join(q)
print(ans)
