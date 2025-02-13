from math import sqrt

D = int(input())
ans = 1 << 60
for x in range(int(sqrt(D)) + 5):
    p = abs(x**2 - D)
    q = int(sqrt(p))
    for y in range(q - 10, q + 10):
        tmp = abs(x**2 + y**2 - D)
        ans = min(ans, tmp)
print(ans)
