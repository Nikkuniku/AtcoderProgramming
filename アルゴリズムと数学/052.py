from math import factorial
x, y = map(int, input().split())
k = (2*x-y)
m = (2*y-x)

mod = 10**9 + 7
ans = 0
if k % 3 == 0 and m % 3 == 0 and k >= 0 and m >= 0:
    k //= 3
    m //= 3
    ans = 1
    for i in range(m+1, k+m+1, 1):
        ans *= i
        ans %= mod
    ans *= pow(factorial(k), mod-2, mod)
    ans %= mod
print(ans)
