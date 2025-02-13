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


# 素数判定
def isPrime(n: int):
    # validation chech
    if n < 0:
        raise ("[ERROR] parameter must be not less than 0 (n >= 0)")

    if n == 0 or n == 1:
        return False
    for i in range(2, n + 1):
        # √N以下まで見ればいい。i*iとして比較するのは小数を扱いたくないため。
        if i * i > n:
            return True
        if n % i == 0:
            return False


A, B = map(int, input().split())
primesA = set(make_divisors(A))
primesB = set(make_divisors(B))
S = primesA & primesB
ans = 1
for s in S:
    ans += isPrime(s)
print(ans)
