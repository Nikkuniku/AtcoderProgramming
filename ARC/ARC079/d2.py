K = int(input())
N = 50
ans = []
if K % N == 0:
    for _ in range(N):
        ans.append(N + (K // N) - 1)
else:
    a = K % N
    for _ in range(a):
        ans.append(N + (K // N))
    for _ in range(N - a):
        ans.append(N + (K // N) - 1 - a)
print(N)
print(*ans)
