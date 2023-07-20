from collections import deque
N = int(input())
A = list(map(int, input().split()))
A.sort()
X, Y = deque(), deque()
for i in range(N):
    if i <= N//2:
        X.append(A[i])
    else:
        Y.append(A[i])
Z = []
for i in range(N):
    if i % 2 == 0:
        Z.append(X.popleft())
    else:
        Z.append(Y.popleft())
ans = 'Yes'
for i in range(N):
    if i % 2 != 0:
        if not (Z[i-1] < Z[i] and Z[i] > Z[i+1]):
            ans = 'No'
print(ans)
