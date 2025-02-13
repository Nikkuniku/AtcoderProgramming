from collections import deque

S = deque(input())
ans = []
for _ in range(len(S)):
    S.rotate()
    ans.append("".join(S))
ans.sort()
print(ans[0])
print(ans[-1])
