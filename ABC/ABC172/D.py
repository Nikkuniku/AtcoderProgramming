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
    return len(lower_divisors) + len(upper_divisors[::-1])


d=[0]*(n+1)

for i in range(n+1):
    d[i]+=make_divisors(i)


ans=0
for i in range(n+1):
    ans+=i*d[i]

print(ans)