def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n=int(input())
p=make_divisors(n)
ans=0
for k in p:
    a1 = n/k -(k-1)/2
    if a1.is_integer():
        ans+=2

print(ans)