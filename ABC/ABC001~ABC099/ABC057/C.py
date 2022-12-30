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


can=make_divisors(n)

ans=10**9

for g in can:
    
    ans=min(ans,max(len(str(g)),len(str(n//g))))


print(ans)