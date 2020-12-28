n,M=map(int,input().split())
a=list(map(int,input().split()))

from itertools import accumulate
import numpy as np

cum=[0]+list(accumulate(a))
# for i in range(n):
#     cum.append(cum[-1]+a[i])

# dp=[[0]*(n+1) for _ in range(M+1)]

dp=np.zeros((M+1,n+1),dtype=float)

for m in range(M+1):
    if m>0:        
        for i in range(m,n+1):
            if m==1:
                dp[m][i]=cum[i]/i
                continue
            else:    
                for j in range(i):
                    dp[m][i]=max(dp[m][i],dp[m-1][j]+ (cum[i]-cum[j])/(i-j))

print(dp[m][n])