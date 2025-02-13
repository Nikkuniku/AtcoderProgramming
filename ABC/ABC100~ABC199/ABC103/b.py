from collections import deque

S = deque(input())
T = input()
ans = "No"
for _ in range(len(S)):
    S.rotate()
    if "".join(S) == T:
        ans = "Yes"
print(ans)
