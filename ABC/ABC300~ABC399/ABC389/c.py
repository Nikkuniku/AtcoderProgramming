from collections import deque

q = deque()
cum = 0
cnt = 0
Q = int(input())
A = [0]
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        l = query[1]
        q.append(l)
        A.append(A[-1] + l)
    elif query[0] == 2:
        m = q.popleft()
        cum += m
        cnt += 1
    elif query[0] == 3:
        k = query[1]
        temp = A[cnt + k - 1] - cum
        ans.append(temp)
print(*ans, sep="\n")
