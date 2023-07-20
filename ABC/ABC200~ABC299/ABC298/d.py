from collections import deque
Q = int(input())
keta = 1
ans = 1
MOD = 998244353
d = deque([1])
res = []
for _ in range(Q):
    query = list(map(int, input().split()))
    i = query[0]
    if i == 1:
        x = query[1]
        ans = 10*ans+x
        ans %= MOD

        keta += 1
        d.append(x)
    elif i == 2:
        v = d.popleft()
        ans = ans-v*pow(10, keta-1, MOD)
        ans %= MOD
        keta -= 1
    else:
        res.append(ans)
print(*res, sep="\n")
