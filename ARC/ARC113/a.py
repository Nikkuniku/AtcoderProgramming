k = int(input())
ans = 0
# 要素がすべて等しい
for a in range(1, 1000):
    if pow(a, 3) <= k:
        ans += 1
# 要素が二つ等しい
for a in range(1, 1000):
    y = k//pow(a, 2)
    if a <= y:
        y -= 1
    ans += 3*y
# 要素が全て異なる
for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = k//(a*b)
        if c > b:
            ans += 6*(c-b)
print(ans)
