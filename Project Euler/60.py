def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def makenum(a, b):
    return int("".join(list(str(a)) + list(str(b))))


def check(k):
    return k % 10 == 7 or k % 10 == 3


from collections import defaultdict

d = defaultdict(set)
S = []
p = 3
while len(S) < 1500:
    if len(make_divisors(p)) == 2:
        for s in S:
            if (
                len(make_divisors(makenum(s, p))) == 2
                and len(make_divisors(makenum(p, s))) == 2
            ):
                d[p].add(s)
        S.append(p)
    p += 2
print(S)
from itertools import combinations

N = 5
Keys = list(d.keys())
for k in Keys:
    if k <= 7927:
        continue
    v = d[k]
    if len(v) >= N - 1:
        print(k, v)
        C = combinations(v, N - 1)
        for c in C:
            isOK = True
            for i in range(N - 1):
                for j in range(i + 1, N - 1):
                    a = c[i]
                    b = c[j]
                    if b > a:
                        a, b = b, a
                    if b not in d[a]:
                        isOK = False
                        break
            if isOK:
                exit(print("***", k, c, "***"))
