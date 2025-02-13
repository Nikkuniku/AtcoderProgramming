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


A = [13, 5701, 5197, 6733, 8389]
CNT = 0
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        p = A[i]
        q = A[j]
        d_pq = make_divisors(makenum(p, q))
        d_qp = make_divisors(makenum(q, p))
        print(makenum(p, q), d_pq)
        print(makenum(q, p), d_qp)
        CNT += 1
print(CNT)
print(sum(A))
