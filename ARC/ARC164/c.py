N = int(input())
CNT = 0
P = []
AB = []
for i in range(N):
    a, b = map(int, input().split())
    if a > b:
        CNT += 1
        P.append((a-b, a, b, i))
    AB.append((a, b, i))
if CNT % 2 == 0:
    ans = sum([max(a, b) for a, b, _ in AB])
else:
    P.sort()
    k, _, _, j = P[0]
    ans = 0
    for i in range(N):
        if i == j:
            ans += min(AB[i][:2])
        else:
            ans += max(AB[i][:2])
print(ans)
