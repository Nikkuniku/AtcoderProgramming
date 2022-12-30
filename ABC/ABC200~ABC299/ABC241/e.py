n, k = map(int, input().split())
a = list(map(int, input().split()))
x = 0
idx = 0
candy = []
dish = []
seen = set()
while True:
    p = a[x % n]
    x = (x+p) % n
    if x in seen:
        candy.append(p)
        break
    else:
        candy.append(p)
        dish.append(x)
        seen.add(x)
idx = dish.index(x)+1

cycle = candy[idx:]
ans = 0
if k > idx:
    ans += sum(candy[:idx])
    k -= idx
    ans += sum(cycle)*(k//len(cycle))
    q = k % len(cycle)
    ans += sum(cycle[:q])
else:
    ans += sum(candy[:k])
print(ans)
