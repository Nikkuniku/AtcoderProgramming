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
p=make_divisors(2*n)
ans=0
for d in p:
    v=2*n//d
    if d%2!=v%2:
        ans+=1

print(ans)