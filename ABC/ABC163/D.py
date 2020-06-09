N,K=map(int,input().split())
mod = (10**9) +7

def counts(n,k):
    if k==1:
        return N+1
    else:
        return k*N - k*( k - 1 ) + 1

total =0
for k in range(K,N+2):
    total += int(counts(N,k))

print(total%mod)