n=int(input())
mod= 998244353
def nums(k):
    re=0
    i=0
    while True:
        if pow(10,i)<=k<pow(10,i+1):
            re+=(k-pow(10,i)+1)*(k-pow(10,i)+2)//2
            re%=mod
            break
        else:
            re+=9*pow(10,i)*(9*pow(10,i)+1)//2
            re%=mod
            i+=1
    
    return re

ans=nums(n)
print(ans)