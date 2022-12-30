from platform import java_ver


a,b,c,d=list(map(int,input().split()))

def eratosthenes(n):
    prime=[True]*(n+1)

    for i in range(2,n+1):
        if not prime[i]:
            continue
            
        p=2*i
        j=i
        while p<n+1:
            prime[p]=False
            p+=j
    
    return prime

isprime=eratosthenes(1000)

ans='Aoki'
for i in range(a,b+1):
    flg=True
    for j in range(c,d+1):
        if isprime[i+j]:
            flg=False

    if flg:
        ans='Takahashi'
        break
print(ans)
