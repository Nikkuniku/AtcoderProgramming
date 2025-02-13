from collections import deque

S = deque(input())
ans = []
for _ in range(2):
    S.rotate()
    ans.append("".join(S))
print(*ans[::-1])
