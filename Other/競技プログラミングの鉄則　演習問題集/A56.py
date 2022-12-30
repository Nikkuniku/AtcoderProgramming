N, Q = map(int, input().split())
S = input()


def alphabetorder(s):
    return ord(s)-96


stringhash = [0]
MOD = 998244353
B = 100
for i in range(N):
    h = (B*stringhash[-1]+alphabetorder(S[i])) % MOD
    stringhash.append(h)
ans = []
pow100 = [1]*(N+1)
for i in range(N+1):
    pow100[i] = pow(B, i, MOD)

for _ in range(Q):
    a, b, c, d = map(lambda x: int(x), input().split())
    h1 = stringhash[b]-pow100[b-a+1]*stringhash[a-1]
    h1 %= MOD
    h2 = stringhash[d]-pow100[d-c+1]*stringhash[c-1]
    h2 %= MOD
    res = 'No'
    if h1 == h2:
        res = 'Yes'
    ans.append(res)
print(*ans, sep="\n")
