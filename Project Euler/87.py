def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


primes = []
M = 50000000
for i in range(2, M):
    if i**2 > M:
        break
    if len(make_divisors(i)) == 2:
        primes.append(i)

squares = []
cubes = []
fourthes = []
for p in primes:
    if p * p <= M:
        squares.append(p * p)
    if p * p * p <= M:
        cubes.append(p * p * p)
    if p * p * p * p <= M:
        fourthes.append(p * p * p * p)
squaresandcubes = set()
for p in squares:
    for q in cubes:
        if p + q <= M:
            squaresandcubes.add(p + q)
ans = 0
for i in range(M + 1):
    for q in fourthes:
        if i - q <= 0:
            break
        if i - q in squaresandcubes:
            ans += 1
            break
print(ans)
