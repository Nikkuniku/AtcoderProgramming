N = int(input())
A = input()[::-1]
B = input()[::-1]
a = 0
b = 0
MOD = 998244353
pows = [pow(10, i, MOD) for i in range(N)]

for i in range(N):
    digita = int(A[i])
    digitb = int(B[i])
    plusa = 0
    plusb = 0
    if A[i] < B[i]:
        plusa = (pows[i]*(digita)) % MOD
        plusb = (pows[i]*(digitb)) % MOD
    else:
        plusa = (pows[i]*(digitb)) % MOD
        plusb = (pows[i]*(digita)) % MOD
    a += plusa
    b += plusb
    a %= MOD
    b %= MOD
ans = a*b % MOD
print(ans)
