from collections import deque

N = int(input())
A = sorted(list(map(int, input().split())))
q = deque(A)
x, y = 0, 0
First = True
while q:
    if First:
        x += q.pop()
    else:
        y += q.popleft()
    First ^= False
print(x - y)
