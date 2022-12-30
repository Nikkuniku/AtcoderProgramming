from itertools import combinations


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


n = int(input())
primes = sieve_of_eratosthenes(55555)
ans = []
for p in primes:
    if p % 10 == 1:
        ans.append(p)

print(ans[:55])
print(len(ans[:55]))
