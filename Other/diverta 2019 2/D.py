n=int(input())

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

arr = make_divisors(n)
total=0
for m in arr:
    r = n//m

    if r<m-1:
        total +=m-1


print(total)
