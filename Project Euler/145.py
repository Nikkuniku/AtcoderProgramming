def AllDigitsAreOdd(n):
    while n > 0:
        if (n % 10) % 2 == 0:
            return False
        n //= 10
    return True


def GetReversible(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    res = 0
    for d in digits:
        res *= 10
        res += d
    return res


N = 1000_000_000
isReversible = [False] * N
for i in range(1, N):
    if isReversible[i]:
        continue
    if i % 10 == 0:
        continue
    rev = GetReversible(i)
    if AllDigitsAreOdd(i + rev):
        isReversible[i] = isReversible[rev] = True
ans = sum(isReversible)
print(ans)
