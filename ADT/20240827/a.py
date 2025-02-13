N, K, A = map(int, input().split())
now = A
while K:
    K -= 1
    if K == 0:
        break
    now += 1
    if now == N + 1:
        now = 1
print(now)
