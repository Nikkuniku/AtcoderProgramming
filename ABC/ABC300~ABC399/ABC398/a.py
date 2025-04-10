from collections import deque

N = int(input())
ans = deque()
if N % 2 == 0:
    ans.append("=")
    ans.append("=")
    N -= 2
else:
    ans.append("=")
    N -= 1
for k in range(N // 2):
    ans.append("-")
    ans.appendleft("-")
print(*ans, sep="")
