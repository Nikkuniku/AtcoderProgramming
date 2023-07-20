def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())
res = set()

for x in range(N):
    if x**2 > N:
        break
    Q = N + x**2
    P = make_divisors(Q)
    for a in P:
        y = a-x
        z = (Q//a)-x
        if y >= 0 and z >= 0:
            if x*y + y*z + z*x == N:
                res.add((x, y, z))
                res.add((x, z, y))
                res.add((y, z, x))
                res.add((y, x, z))
                res.add((z, x, y))
                res.add((z, y, x))
print(len(res))
for c in res:
    print(*c)
