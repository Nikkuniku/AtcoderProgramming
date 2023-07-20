from collections import deque
N = int(input())
X = list(map(int, input().split()))
X.sort()
d = deque(X)
for _ in range(N):
    d.pop()
    d.popleft()
ans = 0
for i in range(len(d)):
    ans += d[i]
ans /= len(d)
print(ans)
