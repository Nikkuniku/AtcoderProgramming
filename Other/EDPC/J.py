n=int(input())
a=list(map(int,input().split()))


n1,n2,n3=0,0,0
for i in range(n):
    if a[i]==1:
        n1+=1
    elif a[i]==2:
        n2+=1
    else:
        n3+=1


dp=[[[0,0]*(n+2) for _ in range(n+2)] for _ in range(n+2) ]
dp[0][0][0]=0.0

for k in range(n+1):
    for j in range(n+1):
        for i in range(n+1):
            x=i+j+k
            p,q,r=0,0,0
            if x==0:
                continue
            if i>0:
                p=dp[k][i-1][j]
            if j>0:
                q=dp[k][i+1][j-1]
            if k>0:
                r=dp[k-1][i][j+1]

            dp[k][i][j] = (i*p + j*q + k*r + n )/x
            
            # print(dp[n3][n1])


print(dp[n3][n1][n2])