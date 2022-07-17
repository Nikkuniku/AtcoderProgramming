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


n, k = map(int, input().split())
s = input()

divs = make_divisors(n)
divs.pop()
ans=n
from collections import Counter
for p in divs:
    tmp_k=0
    for i in range(p):
        tmp=[]
        j=i
        while j<n:
            tmp.append(s[j])
            j+=p
        c=Counter(tmp)
        v=c.most_common(1)[0][-1]
        tmp_k+=(n//p)-v
    if tmp_k<=k:
        ans=min(ans,p)
print(ans)
    