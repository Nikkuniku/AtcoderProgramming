from collections import deque

S = deque(input())
ans = []
for i in range(len(S)):
    ans.append("".join(S))
    S.rotate()
ans.sort()
print(ans[0])
print(ans[-1])
