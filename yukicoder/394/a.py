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


print('? 1', flush=True)
i = int(input())
if i == 0:
    print('! 0 1', flush=True)
A = i-1
print('? 100', flush=True)
j = int(input())
P = make_divisors(100+A-j)
for B in P:
    if j < B and (1+A) % B == i and (100+A) % B == j:
        print('! {} {}'.format(A, B))
