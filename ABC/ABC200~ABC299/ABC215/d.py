n,m=map(int,input().split())
a=list(map(int,input().split()))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

divisor=set()
for b in a:
    divisor|=set(make_divisors(b))

divisor=sorted(list(divisor))[1:]

dp=[False]*(m+1)

for c in divisor:
    j=c
    while c<=m:
        dp[c]=True
        c+=j

cnt=0
answer=[]
for i in range(1,len(dp)):
    if dp[i]!=True:
        answer.append(i)
        cnt+=1

print(cnt)
print(*answer,sep="\n")
