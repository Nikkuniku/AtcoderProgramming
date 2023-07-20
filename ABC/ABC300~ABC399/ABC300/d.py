from bisect import bisect_right
N = int(input())


def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x, 0.5))
    for i in range(2, root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes


primes = sieve_of_eratosthenes(10**6+10)
primes_set = set(primes)
M = len(primes)
ans = 0
for a in range(2, N):
    if a**5 > N:
        break
    if a not in primes_set:
        continue
    for b in range(a+1, N):
        if b**3 > N:
            break
        if b not in primes_set:
            continue
        l = 0
        r = M-1
        while r-l > 1:
            mid = (l+r)//2
            c = primes[mid]
            if a*a*b*c*c <= N:
                l = mid
            else:
                r = mid
        c = primes[l]
        if b < c and a*a*b*c*c <= N:
            idx = bisect_right(primes, b)
            ans += l-idx+1

print(ans)
