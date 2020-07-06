n=int(input())
a=list(map(int,input().split()))
ans=[0]*n
totals=[0]*n


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


for i in range(n-1,-1,-1):
    if totals[i]%2==a[i]:
        continue
    else:
        ans[i]+=1
        arr=make_divisors(i+1)

        for num in arr:
            totals[num-1]+=1

cnt=ans.count(1)

print(cnt)
if cnt!=0:
    b=[]
    for j in range(n):
        if ans[j]!=0:
            b.append(j+1)

    print(*b)
    
