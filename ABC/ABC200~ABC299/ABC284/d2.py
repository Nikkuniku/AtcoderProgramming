
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


primes = sieve_of_eratosthenes(3*pow(10, 6))
primes_set = set(primes)


def solve(n):
    for i in primes:
        if n % (i**2) == 0:
            q = n//(i**2)
            if i != q:
                return i, q
        if n % i == 0:
            p = pow(n//i, 0.5)
            if p.is_integer():
                if int(p) != i:
                    return int(p), i


ans = []
T = int(input())
for _ in range(T):
    N = int(input())
    ans.append(solve(N))
for a in ans:
    print(*a)
