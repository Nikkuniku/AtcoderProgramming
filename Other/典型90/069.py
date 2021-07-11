N,K=map(int,input().split())
mod=10**9 +7



if K==1:
    if N==1:
        ans=1
    else:
        ans=0
elif K==2:
    if N<=2:
        ans=K
    else:
        ans=0
else: 
    if N>=2:
        ans=(K%mod)*((K-1)%mod)*pow(K-2,N-2,mod)
    else:
        ans=K

print(ans%mod)