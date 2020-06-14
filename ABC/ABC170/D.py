n=int(input())
a=list(map(int,input().split()))

a=sorted(a)

dp=[0]*(max(a)+1)

cnt=0
for i in range(n):
    b=a[i]
    dp[b]+=1

    while b<=max(a):
        b+=b
        dp[b]+=1


for i in range(len(dp)):
    if dp[i]==1:
        cnt+=1

print(cnt)