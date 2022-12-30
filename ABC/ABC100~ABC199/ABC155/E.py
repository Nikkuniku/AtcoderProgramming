N = input()[::-1]
M = len(N)
ans = 0
plus = 0
for i in range(M):
    k = int(N[i])
    k += plus
    if 0 <= k <= 5:
        ans += k
        plus = 0
    elif 6 <= k <= 9:
        ans += 10-k
        plus = 1
    elif k == 10:
        plus = 1
if plus == 1:
    ans += 1
print(ans)
