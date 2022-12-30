N, Q = map(int, input().split())
S = input()
revS = S[::-1]
MOD = 998244353
LeftHash = [0]
RightHash = [0]
B = 100
powers = [1]*(N+1)
for i in range(1, N+1):
    powers[i] *= B*powers[i-1]
    powers[i] %= MOD

for i in range(N):
    hl = B*LeftHash[-1]+ord(S[i])
    hr = B*RightHash[-1]+ord(revS[i])
    LeftHash.append(hl % MOD)
    RightHash.append(hr % MOD)

ans = []
for _ in range(Q):
    L, R = map(int, input().split())
    revL, revR = N-R+1, N-L+1
    h1 = (LeftHash[R]-powers[R-L+1]*LeftHash[L-1]) % MOD
    h2 = (RightHash[revR]-powers[revR-revL+1]*RightHash[revL-1]) % MOD
    res = 'No'
    if h1 == h2:
        res = 'Yes'
    ans.append(res)
print(*ans, sep="\n")
