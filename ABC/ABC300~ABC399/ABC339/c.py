N = int(input())
A = list(map(int, input().split()))
B = []
now = 0
for v in A:
    now += v
    B.append(now)
M = min(B)
ans = B[-1]
if M < 0:
    ans += -M
print(ans)
