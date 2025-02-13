N = int(input())
A = list(map(int, input().split()))
ans = 0
res = 1 << 60
for a in A:
    ans += a
    res = min(res, ans)
if res < 0:
    ans += -res
print(ans)
