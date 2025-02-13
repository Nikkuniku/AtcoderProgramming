from collections import deque

S = input()
q = deque(S)
ans = []
for _ in range(len(S)):
    q.rotate()
    ans.append("".join(q))
ans.sort()
print(ans[0])
print(ans[-1])
