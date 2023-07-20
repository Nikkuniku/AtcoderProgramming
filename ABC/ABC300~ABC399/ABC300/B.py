from collections import deque
H, W = map(int, input().split())
A = deque([deque(input()) for _ in range(H)])
B = deque([deque(input()) for _ in range(H)])
ans = 'No'
for _ in range(H+1):
    A.rotate()
    for i in range(W+1):
        for j in range(H):
            A[j].rotate()
        if A == B:
            ans = 'Yes'
print(ans)
