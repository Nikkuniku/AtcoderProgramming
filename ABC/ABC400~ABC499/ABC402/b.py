from collections import deque

Q = int(input())
ans = []
d = deque()
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        d.append(query[1])
    elif query[0] == 2:
        ans.append(d.popleft())
print(*ans, sep="\n")
