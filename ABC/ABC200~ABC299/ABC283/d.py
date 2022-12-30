from collections import deque, defaultdict
S = input()
q = deque([])
d = defaultdict(lambda: 0)
ans = 'Yes'
for i in range(len(S)):
    s = S[i]
    if s == '(':
        q.append(s)
    elif s == ')':
        while True:
            v = q.pop()
            if v == '(':
                break
            else:
                d[v] -= 1
    else:
        if d[s] > 0:
            ans = 'No'
            break
        else:
            d[s] += 1
            q.append(s)
print(ans)
