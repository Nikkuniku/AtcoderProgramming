n=int(input())

def sum_k(n):
    return n*(n+1)//2

ans=0
for i in range(1,n+1):
    ans+=i*sum_k(n//i)

print(ans)