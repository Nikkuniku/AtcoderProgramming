k=int(input())

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

p=make_divisors(k)
m=len(p)
s=set(p)
ans=0
for q in p:
    if k%pow(q,2)==0:
        a = k//pow(q,2)
        if a in s:
            ans+=1

if m>1:
    for i in range(m):
        for j in range(i+1,m):
            if k%(p[i]*p[j])==0:
                c = k//(p[i]*p[j])
                if c in s and p[j]<c:
                    ans+=1

print(ans)