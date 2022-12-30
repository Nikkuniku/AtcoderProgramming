n, k = map(int, input().split())
a = list(map(int, input().split()))
x = 0
p = 0
candy = []
seen = set()
while True:
    p = a[x % n]
    if p in seen:
        break
    else:
        candy.append(p)
        seen.add(p)
        x += p
idx = candy.index(p)
cycle = candy[idx:]
ans = 0
if k <= idx:
    ans += sum(candy[:idx])
else:
    ans += sum(candy[:idx])
    k -= idx
    ans += sum(cycle)*(k//len(cycle))
    q = k % len(cycle)
    ans += sum(cycle[:q])
print(ans)
