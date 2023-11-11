N = int(input())
A = list(map(int, input().split()))
P = [0]*361
now = 0
P[0] = P[360] = 1
for i in range(N):
    now = (now-A[i]) % 360
    P[now] = 1
ans = []
prev = 0
for i in range(361):
    if P[i] == 1:
        ans.append(i-prev)
        prev = i
print(max(ans))
