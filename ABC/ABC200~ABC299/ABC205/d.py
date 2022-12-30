n,q=map(int,input().split())
a=[0]+list(map(int,input().split()))
cum_sum=[0]
dif = [0]
for i in range(n):
    dif.append(a[i+1] - a[i] - 1)
    cum_sum.append(cum_sum[-1] + dif[i+1])

from bisect import bisect_left

answer=[]
for _ in range(q):
    k=int(input())
    i = bisect_left(cum_sum,k)
    ans= a[i-1] + (k-cum_sum[i-1])
    answer.append(ans)

print(*answer,sep="\n")