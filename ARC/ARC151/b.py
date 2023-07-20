N, M = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))
Pidx = [-1]*N
for i in range(N):
    Pidx[P[i]] = i
Q = [False]*N
ans = 0
nondecided = N
MOD = 998244353
for i in range(N):
    if i == P[i]:
        Q[i] = True
        nondecided -= 1
    else:
        if not Q[i] or not Q[P[i]]:
            if not Q[i]:
                Q[i] = True
                nondecided -= 1
            if not Q[P[i]]:
                Q[P[i]] = True
                nondecided -= 1
            Q[i] = True
            ans += ((M*(M-1)//2))*pow(M, nondecided, MOD)
            ans %= MOD
print(ans)
