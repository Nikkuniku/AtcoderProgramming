N, M = map(int, input().split())
INF = 1 << 60
ans = INF
for a in range(1, int(M**0.5) + 2):
    if a > N:
        break
    b = (M + a - 1) // a
    if b > N:
        continue
    if M <= a * b:
        ans = min(ans, a * b)
if ans == INF:
    ans = -1
print(ans)
