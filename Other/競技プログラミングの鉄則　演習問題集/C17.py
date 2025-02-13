from collections import deque

Q = int(input())

front = deque()
back = deque()
ans = []
for _ in range(Q):
    query = list(input().split())
    if query[0] == "A":
        x = query[1]
        back.append(x)
    elif query[0] == "B":
        x = query[1]
        back.appendleft(x)
    elif query[0] == "C":
        front.popleft()
    elif query[0] == "D":
        ans.append(front[0])
    M = len(front) + len(back)
    if M % 2 == 0:
        while len(front) < M // 2:
            front.append(back.popleft())
    else:
        while len(front) < (M + 1) // 2:
            front.append(back.popleft())
print(*ans, sep="\n")
